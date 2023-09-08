;; Auto-generated. Do not edit!


(when (boundp 'test_get_image::zsrMsg)
  (if (not (find-package "TEST_GET_IMAGE"))
    (make-package "TEST_GET_IMAGE"))
  (shadow 'zsrMsg (find-package "TEST_GET_IMAGE")))
(unless (find-package "TEST_GET_IMAGE::ZSRMSG")
  (make-package "TEST_GET_IMAGE::ZSRMSG"))

(in-package "ROS")
;;//! \htmlinclude zsrMsg.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass test_get_image::zsrMsg
  :super ros::object
  :slots (_utcTime _latitude _longitude _altitude _heading _propertyType _measure _feature _process _parameter _resultQuality _OrchardID _CameraID _SecondaryCameraID _ImageID _SecondaryImageID _INSlatitude _INSlongitude _INSaltitude _INStime ))

(defmethod test_get_image::zsrMsg
  (:init
   (&key
    ((:utcTime __utcTime) 0.0)
    ((:latitude __latitude) 0.0)
    ((:longitude __longitude) 0.0)
    ((:altitude __altitude) 0.0)
    ((:heading __heading) 0.0)
    ((:propertyType __propertyType) (instance std_msgs::String :init))
    ((:measure __measure) 0.0)
    ((:feature __feature) (instance std_msgs::String :init))
    ((:process __process) (instance std_msgs::String :init))
    ((:parameter __parameter) (instance std_msgs::String :init))
    ((:resultQuality __resultQuality) (instance std_msgs::String :init))
    ((:OrchardID __OrchardID) (instance std_msgs::String :init))
    ((:CameraID __CameraID) (instance std_msgs::String :init))
    ((:SecondaryCameraID __SecondaryCameraID) (instance std_msgs::String :init))
    ((:ImageID __ImageID) (instance std_msgs::String :init))
    ((:SecondaryImageID __SecondaryImageID) (instance std_msgs::String :init))
    ((:INSlatitude __INSlatitude) 0.0)
    ((:INSlongitude __INSlongitude) 0.0)
    ((:INSaltitude __INSaltitude) 0.0)
    ((:INStime __INStime) 0.0)
    )
   (send-super :init)
   (setq _utcTime (float __utcTime))
   (setq _latitude (float __latitude))
   (setq _longitude (float __longitude))
   (setq _altitude (float __altitude))
   (setq _heading (float __heading))
   (setq _propertyType __propertyType)
   (setq _measure (float __measure))
   (setq _feature __feature)
   (setq _process __process)
   (setq _parameter __parameter)
   (setq _resultQuality __resultQuality)
   (setq _OrchardID __OrchardID)
   (setq _CameraID __CameraID)
   (setq _SecondaryCameraID __SecondaryCameraID)
   (setq _ImageID __ImageID)
   (setq _SecondaryImageID __SecondaryImageID)
   (setq _INSlatitude (float __INSlatitude))
   (setq _INSlongitude (float __INSlongitude))
   (setq _INSaltitude (float __INSaltitude))
   (setq _INStime (float __INStime))
   self)
  (:utcTime
   (&optional __utcTime)
   (if __utcTime (setq _utcTime __utcTime)) _utcTime)
  (:latitude
   (&optional __latitude)
   (if __latitude (setq _latitude __latitude)) _latitude)
  (:longitude
   (&optional __longitude)
   (if __longitude (setq _longitude __longitude)) _longitude)
  (:altitude
   (&optional __altitude)
   (if __altitude (setq _altitude __altitude)) _altitude)
  (:heading
   (&optional __heading)
   (if __heading (setq _heading __heading)) _heading)
  (:propertyType
   (&rest __propertyType)
   (if (keywordp (car __propertyType))
       (send* _propertyType __propertyType)
     (progn
       (if __propertyType (setq _propertyType (car __propertyType)))
       _propertyType)))
  (:measure
   (&optional __measure)
   (if __measure (setq _measure __measure)) _measure)
  (:feature
   (&rest __feature)
   (if (keywordp (car __feature))
       (send* _feature __feature)
     (progn
       (if __feature (setq _feature (car __feature)))
       _feature)))
  (:process
   (&rest __process)
   (if (keywordp (car __process))
       (send* _process __process)
     (progn
       (if __process (setq _process (car __process)))
       _process)))
  (:parameter
   (&rest __parameter)
   (if (keywordp (car __parameter))
       (send* _parameter __parameter)
     (progn
       (if __parameter (setq _parameter (car __parameter)))
       _parameter)))
  (:resultQuality
   (&rest __resultQuality)
   (if (keywordp (car __resultQuality))
       (send* _resultQuality __resultQuality)
     (progn
       (if __resultQuality (setq _resultQuality (car __resultQuality)))
       _resultQuality)))
  (:OrchardID
   (&rest __OrchardID)
   (if (keywordp (car __OrchardID))
       (send* _OrchardID __OrchardID)
     (progn
       (if __OrchardID (setq _OrchardID (car __OrchardID)))
       _OrchardID)))
  (:CameraID
   (&rest __CameraID)
   (if (keywordp (car __CameraID))
       (send* _CameraID __CameraID)
     (progn
       (if __CameraID (setq _CameraID (car __CameraID)))
       _CameraID)))
  (:SecondaryCameraID
   (&rest __SecondaryCameraID)
   (if (keywordp (car __SecondaryCameraID))
       (send* _SecondaryCameraID __SecondaryCameraID)
     (progn
       (if __SecondaryCameraID (setq _SecondaryCameraID (car __SecondaryCameraID)))
       _SecondaryCameraID)))
  (:ImageID
   (&rest __ImageID)
   (if (keywordp (car __ImageID))
       (send* _ImageID __ImageID)
     (progn
       (if __ImageID (setq _ImageID (car __ImageID)))
       _ImageID)))
  (:SecondaryImageID
   (&rest __SecondaryImageID)
   (if (keywordp (car __SecondaryImageID))
       (send* _SecondaryImageID __SecondaryImageID)
     (progn
       (if __SecondaryImageID (setq _SecondaryImageID (car __SecondaryImageID)))
       _SecondaryImageID)))
  (:INSlatitude
   (&optional __INSlatitude)
   (if __INSlatitude (setq _INSlatitude __INSlatitude)) _INSlatitude)
  (:INSlongitude
   (&optional __INSlongitude)
   (if __INSlongitude (setq _INSlongitude __INSlongitude)) _INSlongitude)
  (:INSaltitude
   (&optional __INSaltitude)
   (if __INSaltitude (setq _INSaltitude __INSaltitude)) _INSaltitude)
  (:INStime
   (&optional __INStime)
   (if __INStime (setq _INStime __INStime)) _INStime)
  (:serialization-length
   ()
   (+
    ;; float64 _utcTime
    8
    ;; float64 _latitude
    8
    ;; float64 _longitude
    8
    ;; float64 _altitude
    8
    ;; float64 _heading
    8
    ;; std_msgs/String _propertyType
    (send _propertyType :serialization-length)
    ;; float64 _measure
    8
    ;; std_msgs/String _feature
    (send _feature :serialization-length)
    ;; std_msgs/String _process
    (send _process :serialization-length)
    ;; std_msgs/String _parameter
    (send _parameter :serialization-length)
    ;; std_msgs/String _resultQuality
    (send _resultQuality :serialization-length)
    ;; std_msgs/String _OrchardID
    (send _OrchardID :serialization-length)
    ;; std_msgs/String _CameraID
    (send _CameraID :serialization-length)
    ;; std_msgs/String _SecondaryCameraID
    (send _SecondaryCameraID :serialization-length)
    ;; std_msgs/String _ImageID
    (send _ImageID :serialization-length)
    ;; std_msgs/String _SecondaryImageID
    (send _SecondaryImageID :serialization-length)
    ;; float64 _INSlatitude
    8
    ;; float64 _INSlongitude
    8
    ;; float64 _INSaltitude
    8
    ;; float64 _INStime
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _utcTime
       (sys::poke _utcTime (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _latitude
       (sys::poke _latitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _longitude
       (sys::poke _longitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _altitude
       (sys::poke _altitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _heading
       (sys::poke _heading (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; std_msgs/String _propertyType
       (send _propertyType :serialize s)
     ;; float64 _measure
       (sys::poke _measure (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; std_msgs/String _feature
       (send _feature :serialize s)
     ;; std_msgs/String _process
       (send _process :serialize s)
     ;; std_msgs/String _parameter
       (send _parameter :serialize s)
     ;; std_msgs/String _resultQuality
       (send _resultQuality :serialize s)
     ;; std_msgs/String _OrchardID
       (send _OrchardID :serialize s)
     ;; std_msgs/String _CameraID
       (send _CameraID :serialize s)
     ;; std_msgs/String _SecondaryCameraID
       (send _SecondaryCameraID :serialize s)
     ;; std_msgs/String _ImageID
       (send _ImageID :serialize s)
     ;; std_msgs/String _SecondaryImageID
       (send _SecondaryImageID :serialize s)
     ;; float64 _INSlatitude
       (sys::poke _INSlatitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _INSlongitude
       (sys::poke _INSlongitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _INSaltitude
       (sys::poke _INSaltitude (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _INStime
       (sys::poke _INStime (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _utcTime
     (setq _utcTime (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _latitude
     (setq _latitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _longitude
     (setq _longitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _altitude
     (setq _altitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _heading
     (setq _heading (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; std_msgs/String _propertyType
     (send _propertyType :deserialize buf ptr-) (incf ptr- (send _propertyType :serialization-length))
   ;; float64 _measure
     (setq _measure (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; std_msgs/String _feature
     (send _feature :deserialize buf ptr-) (incf ptr- (send _feature :serialization-length))
   ;; std_msgs/String _process
     (send _process :deserialize buf ptr-) (incf ptr- (send _process :serialization-length))
   ;; std_msgs/String _parameter
     (send _parameter :deserialize buf ptr-) (incf ptr- (send _parameter :serialization-length))
   ;; std_msgs/String _resultQuality
     (send _resultQuality :deserialize buf ptr-) (incf ptr- (send _resultQuality :serialization-length))
   ;; std_msgs/String _OrchardID
     (send _OrchardID :deserialize buf ptr-) (incf ptr- (send _OrchardID :serialization-length))
   ;; std_msgs/String _CameraID
     (send _CameraID :deserialize buf ptr-) (incf ptr- (send _CameraID :serialization-length))
   ;; std_msgs/String _SecondaryCameraID
     (send _SecondaryCameraID :deserialize buf ptr-) (incf ptr- (send _SecondaryCameraID :serialization-length))
   ;; std_msgs/String _ImageID
     (send _ImageID :deserialize buf ptr-) (incf ptr- (send _ImageID :serialization-length))
   ;; std_msgs/String _SecondaryImageID
     (send _SecondaryImageID :deserialize buf ptr-) (incf ptr- (send _SecondaryImageID :serialization-length))
   ;; float64 _INSlatitude
     (setq _INSlatitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _INSlongitude
     (setq _INSlongitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _INSaltitude
     (setq _INSaltitude (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _INStime
     (setq _INStime (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get test_get_image::zsrMsg :md5sum-) "8acb67a9b0a2fd36aee93ed2e2fde2cc")
(setf (get test_get_image::zsrMsg :datatype-) "test_get_image/zsrMsg")
(setf (get test_get_image::zsrMsg :definition-)
      "float64             utcTime
float64             latitude
float64             longitude
float64             altitude
float64             heading

std_msgs/String     propertyType
float64             measure

std_msgs/String     feature
std_msgs/String     process
std_msgs/String     parameter
std_msgs/String     resultQuality

std_msgs/String     OrchardID
std_msgs/String     CameraID
std_msgs/String     SecondaryCameraID
std_msgs/String     ImageID
std_msgs/String     SecondaryImageID

float64             INSlatitude
float64             INSlongitude
float64             INSaltitude
float64             INStime

================================================================================
MSG: std_msgs/String
string data

")



(provide :test_get_image/zsrMsg "8acb67a9b0a2fd36aee93ed2e2fde2cc")


