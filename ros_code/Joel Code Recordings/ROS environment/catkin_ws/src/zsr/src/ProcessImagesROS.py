#!/usr/bin/python3

import rospy
from zsr.msg import zsrMsg
import redis
from opex import ObjectPredictions
import time
import numpy as np
import yaml
import cv2
import os
from shapely import geometry
import math
import pickle

ConfigLocation = "/home/billy/CameraConfigs/"
ImageLocation = "/media/externaldrive/CompletedRuns/"
ImageQueue = []
r = redis.Redis(host="localhost", port=6379, db=0)
p = r.pubsub()

def ReceiveImages(data):
    if (data.resultQuality.data == "Unprocessed"):
        ImageQueue.append(data)

def PredictionHandler(Message):
    global Predictions
    JSONString = Message['data'].decode()
    Predictions = ObjectPredictions.from_json_string(JSONString)

def GetConfigs():
    global CameraParams
    CameraParams = {}
    Configs = [Config for Config in os.listdir(ConfigLocation) if (Config[-5:] == '.yaml')]
    for Config in Configs:
        with open(ConfigLocation + Config, "r") as stream:
            calib = yaml.safe_load(stream)
        calibK = np.array(calib['camera_matrix']['data']).reshape((3,3))
        calibD = np.array(calib['distortion_coefficients']['data']).reshape((1,5))
        calibP = np.array(calib['projection_matrix']['data']).reshape((3,3))
        calibR = np.array(calib['rectification_matrix']['data']).reshape((3,3))
        calibMainBaseline = float(calib['maincambaseline'])
        calibWidth = calib['image_width']
        calibHeight = calib['image_height']
        AOVHorizontal = float(calib['AOVHorizontal'])
        AOVVertical = float(calib['AOVVertical'])
        MapX, MapY = cv2.initUndistortRectifyMap(calibK,calibD,calibR,calibP,(calibWidth,calibHeight),5)
        CameraParams[Config[:-5]] = {'Intrinsic': calibK, 'Distortion': calibD, 'Projection': calibP, 'MainCamBaseline': calibMainBaseline, 'ImageWidth': calibWidth, 'ImageHeight': calibHeight, 'AOVHorizontal': AOVHorizontal, 'AOVVertical': AOVVertical, 'MapX': MapX, 'MapY': MapY}
        
    for Camera in CameraParams:
        if Camera[-1] == "R":
            CameraParams[Camera]['Baseline'] = float(calibMainBaseline - CameraParams[Camera[:-1]+"L"]['MainCamBaseline'])

def CheckBackup():
    global ImageQueue
    try:
        with open(ImageLocation + "ImageQueue", 'rb') as f:
            ImageQueue = pickle.load(f)
        os.remove(ImageLocation + "ImageQueue")
    except:
        print("No backup exists, waiting for images...")

def GetDisparity(UndistortedImage,SecondaryUndistortedImage):
    #Generate Disparity Map
    LeftGrey = cv2.cvtColor(UndistortedImage, cv2.COLOR_BGR2GRAY)
    RightGrey = cv2.cvtColor(SecondaryUndistortedImage, cv2.COLOR_BGR2GRAY)
    Matcher = cv2.StereoSGBM_create(minDisparity=0,numDisparities=32,blockSize=5,P1=43,P2=85,disp12MaxDiff=-1,uniquenessRatio=11,speckleWindowSize=256,speckleRange=7,preFilterCap=63,mode=cv2.STEREO_SGBM_MODE_SGBM_3WAY)
    SecondaryMatcher = cv2.ximgproc.createRightMatcher(Matcher)
    Disparity = Matcher.compute(LeftGrey, RightGrey)
    SecondaryDisparity = SecondaryMatcher.compute(RightGrey, LeftGrey)
    wls_filter = cv2.ximgproc.createDisparityWLSFilter(Matcher)
    FilteredDisparity = wls_filter.filter(Disparity, LeftGrey, disparity_map_right=SecondaryDisparity)
    FilteredDisparity = FilteredDisparity.astype(np.float32)/16.0
    FilteredDisparity[FilteredDisparity < 0] = 0
    return(FilteredDisparity)

def GetObjectLocations(ObjectBoundingBoxes,ObjectPolygons,DisparityMap,CameraID,SecondaryCameraID):
    Baseline = CameraParams[SecondaryCameraID]['Baseline']
    FocalLength = CameraParams[SecondaryCameraID]['Projection'][0,0]
    ImageWidth = CameraParams[SecondaryCameraID]['ImageWidth']
    ImageHeight = CameraParams[SecondaryCameraID]['ImageHeight']
    CentrePointX = CameraParams[CameraID]['Projection'][0,2]
    CentrePointY = CameraParams[CameraID]['Projection'][1,2]
    AOVHorizontal = CameraParams[CameraID]['AOVHorizontal']
    AOVVertical = CameraParams[CameraID]['AOVVertical']

    BudWorldLocations = []
    for Polygon in ObjectPolygons:
        try:
            Bounds,BudWorldLocations = [],[]
            for Point in Polygon:
                Bounds.append((int(Point[1]),int(Point[0])))
            Poly = geometry.Polygon(Bounds)
            PolyCentroidX = int(Poly.centroid.x); PolyCentroidY = int(Poly.centroid.y)
            BudCentreWindow = DisparityMap[PolyCentroidY-5:PolyCentroidY+5,PolyCentroidX-5:PolyCentroidX+5]; BudCentreDisparity = np.mean(BudCentreWindow[np.logical_and(BudCentreWindow>0,BudCentreWindow<1000)])
            PolyWorldZ = Baseline*FocalLength/BudCentreDisparity #Depth = Baseline*FocalLength/Disparity
            PolyWorldX = PolyWorldZ*math.tan(math.radians(((PolyCentroidX-CentrePointX)/ImageWidth)*AOVHorizontal))
            PolyWorldY = PolyWorldZ*math.tan(math.radians(((PolyCentroidY-CentrePointY)/ImageHeight)*AOVVertical))
            BudWorldLocations.append([PolyWorldX,PolyWorldY,PolyWorldZ])
        except:
            pass
    return(BudWorldLocations)
        
def LocateBuds():
    global Predictions
    QueueSaved = False
    while True:
        try:
            if len(ImageQueue):
                print("Processing")
                StartTime = time.time()
                #Read zsrMsg parameters
                message = ImageQueue[0]
                FolderName = message.OrchardID.data
                CameraID = message.CameraID.data
                SecondaryCameraID = message.SecondaryCameraID.data
                FileName = message.ImageID.data

                #Read images associated with message and undistort
                FilePath = ImageLocation + FolderName + "/" + FileName
                RectifiedFilePath = FilePath[:-4] + "_Processed.jpg"
                RawImage = cv2.imread(FilePath)
                UndistortedImage = cv2.remap(RawImage,CameraParams[CameraID]['MapX'],CameraParams[CameraID]['MapY'],cv2.INTER_LINEAR)
                #cv2.imwrite(RectifiedFilePath, UndistortedImage)

                #Send primary image to Detectron Redis channel
                ProcessedImage = cv2.imencode('.jpg',UndistortedImage)
                Predictions = False
                r.publish("images", ProcessedImage[1].tobytes())
                ImagePublishedTime = time.time()

                #Generate Disparity Map
                if SecondaryCameraID != "None":
                    SecondaryFileName = message.SecondaryImageID.data
                    SecondaryFilePath = ImageLocation + FolderName + "/" + SecondaryFileName
                    SecondaryRectifiedFilePath = SecondaryFilePath[:-4] + "_Processed.jpg"
                    SecondaryRawImage = cv2.imread(SecondaryFilePath)
                    SecondaryUndistortedImage = cv2.remap(SecondaryRawImage,CameraParams[SecondaryCameraID]['MapX'],CameraParams[SecondaryCameraID]['MapY'],cv2.INTER_LINEAR)
                    DisparityMap = GetDisparity(UndistortedImage,SecondaryUndistortedImage)
                    #cv2.imwrite(SecondaryRectifiedFilePath, SecondaryUndistortedImage)

                #Receive Predictions
                while not Predictions: 
                    if (time.time() - ImagePublishedTime) > 15:
                        print("Docker not responding...")
                        r.publish("images", ProcessedImage[1].tobytes())
                        ImagePublishedTime = time.time()
                        if not QueueSaved:
                            with open(ImageLocation + "ImageQueue", 'wb') as f:
                                pickle.dump(ImageQueue, f)
                            QueueSaved = True
                    time.sleep(0.01)
                if QueueSaved:
                    os.remove(ImageLocation + "ImageQueue")
                    QueueSaved = False

                ObjectBoundingBoxes, ObjectPolygons = [],[]
                for Prediction in Predictions.objects:
                    cv2.rectangle(UndistortedImage,(Prediction.bbox.left,Prediction.bbox.top),(Prediction.bbox.right,Prediction.bbox.bottom),(0,0,255),2)
                    ObjectBoundingBoxes.append([(Prediction.bbox.left,Prediction.bbox.top),(Prediction.bbox.left,Prediction.bbox.bottom),(Prediction.bbox.right,Prediction.bbox.bottom),(Prediction.bbox.right,Prediction.bbox.top)])
                    ObjectPolygons.append(Prediction.polygon.points)
                print(ObjectBoundingBoxes)
                cv2.imwrite(RectifiedFilePath, UndistortedImage)

                #Get world coordinates of identified objects
                if SecondaryCameraID != "None":
                    ObjectLocations = GetObjectLocations(ObjectBoundingBoxes,ObjectPolygons,DisparityMap,CameraID,SecondaryCameraID)

                #Send modified zsrMsg containing predictions
                message.ImageID.data = FileName[:-4] + "_Processed.jpg"
                message.measure = float(len(ObjectBoundingBoxes))
                message.resultQuality.data = "Processed"
                pub.publish(message)
                print("Processed " + FileName + " in " + str(time.time()-StartTime) + "S")
                del ImageQueue[0]
            else:
                time.sleep(0.1)
        except:
            print("Error Occured")
            if not QueueSaved:
                with open(ImageLocation + "ImageQueue", 'wb') as f:
                    pickle.dump(ImageQueue, f)
                QueueSaved = True
            time.sleep(10)

if __name__ == "__main__":
    global pub
    print("Starting")
    GetConfigs()
    CheckBackup()
    p.psubscribe(**{"predictions": PredictionHandler})
    p.run_in_thread(sleep_time=0.001)
    rospy.init_node('LocateObjects', anonymous=True)
    rospy.Subscriber("/zsrMsg", zsrMsg, ReceiveImages)
    pub = rospy.Publisher('/zsrMsg', zsrMsg, queue_size=10)
    LocateBuds()
