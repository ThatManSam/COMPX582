import cv2
from dt_apriltags import Detector

if __name__ == "__main__":
    at_detector = Detector(families='tagStandard52h13',
                        nthreads=1,
                        quad_decimate=1.0,
                        quad_sigma=0.0,
                        refine_edges=1,
                        decode_sharpening=0.25,
                        debug=0)

    img = cv2.imread("./tag52_13_00006.png", cv2.IMREAD_GRAYSCALE)
    tags = at_detector.detect(img)

    color_img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    for tag in tags:
        for idx in range(len(tag.corners)):
            cv2.line(color_img, tuple(tag.corners[idx-1, :].astype(int)), tuple(tag.corners[idx, :].astype(int)), (0, 255, 0))

        cv2.putText(color_img, str(tag.tag_id),
                    org=(tag.corners[0, 0].astype(int)+10,tag.corners[0, 1].astype(int)+10),
                    fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=0.8,
                    color=(0, 0, 255))

    cv2.imshow('Detected tags', color_img)

    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
