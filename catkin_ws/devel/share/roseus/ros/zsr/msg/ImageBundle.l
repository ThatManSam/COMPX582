;; Auto-generated. Do not edit!


(when (boundp 'zsr::ImageBundle)
  (if (not (find-package "ZSR"))
    (make-package "ZSR"))
  (shadow 'ImageBundle (find-package "ZSR")))
(unless (find-package "ZSR::IMAGEBUNDLE")
  (make-package "ZSR::IMAGEBUNDLE"))

(in-package "ROS")
;;//! \htmlinclude ImageBundle.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass zsr::ImageBundle
  :super ros::object
  :slots (_header _DeviceIDs _LLH _Images ))

(defmethod zsr::ImageBundle
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:DeviceIDs __DeviceIDs) ())
    ((:LLH __LLH) (instance geometry_msgs::Vector3 :init))
    ((:Images __Images) ())
    )
   (send-super :init)
   (setq _header __header)
   (setq _DeviceIDs __DeviceIDs)
   (setq _LLH __LLH)
   (setq _Images __Images)
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:DeviceIDs
   (&rest __DeviceIDs)
   (if (keywordp (car __DeviceIDs))
       (send* _DeviceIDs __DeviceIDs)
     (progn
       (if __DeviceIDs (setq _DeviceIDs (car __DeviceIDs)))
       _DeviceIDs)))
  (:LLH
   (&rest __LLH)
   (if (keywordp (car __LLH))
       (send* _LLH __LLH)
     (progn
       (if __LLH (setq _LLH (car __LLH)))
       _LLH)))
  (:Images
   (&rest __Images)
   (if (keywordp (car __Images))
       (send* _Images __Images)
     (progn
       (if __Images (setq _Images (car __Images)))
       _Images)))
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; std_msgs/String[] _DeviceIDs
    (apply #'+ (send-all _DeviceIDs :serialization-length)) 4
    ;; geometry_msgs/Vector3 _LLH
    (send _LLH :serialization-length)
    ;; sensor_msgs/Image[] _Images
    (apply #'+ (send-all _Images :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; std_msgs/String[] _DeviceIDs
     (write-long (length _DeviceIDs) s)
     (dolist (elem _DeviceIDs)
       (send elem :serialize s)
       )
     ;; geometry_msgs/Vector3 _LLH
       (send _LLH :serialize s)
     ;; sensor_msgs/Image[] _Images
     (write-long (length _Images) s)
     (dolist (elem _Images)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; std_msgs/String[] _DeviceIDs
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _DeviceIDs (let (r) (dotimes (i n) (push (instance std_msgs::String :init) r)) r))
     (dolist (elem- _DeviceIDs)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;; geometry_msgs/Vector3 _LLH
     (send _LLH :deserialize buf ptr-) (incf ptr- (send _LLH :serialization-length))
   ;; sensor_msgs/Image[] _Images
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _Images (let (r) (dotimes (i n) (push (instance sensor_msgs::Image :init) r)) r))
     (dolist (elem- _Images)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get zsr::ImageBundle :md5sum-) "c8fb7a8e02d1a79f085a43bf538d089b")
(setf (get zsr::ImageBundle :datatype-) "zsr/ImageBundle")
(setf (get zsr::ImageBundle :definition-)
      "std_msgs/Header           header
std_msgs/String[]        DeviceIDs
geometry_msgs/Vector3     LLH
sensor_msgs/Image[]      Images
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: std_msgs/String
string data

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: sensor_msgs/Image
# This message contains an uncompressed image
# (0, 0) is at top-left corner of image
#

Header header        # Header timestamp should be acquisition time of image
                     # Header frame_id should be optical frame of camera
                     # origin of frame should be optical center of camera
                     # +x should point to the right in the image
                     # +y should point down in the image
                     # +z should point into to plane of the image
                     # If the frame_id here and the frame_id of the CameraInfo
                     # message associated with the image conflict
                     # the behavior is undefined

uint32 height         # image height, that is, number of rows
uint32 width          # image width, that is, number of columns

# The legal values for encoding are in file src/image_encodings.cpp
# If you want to standardize a new string format, join
# ros-users@lists.sourceforge.net and send an email proposing a new encoding.

string encoding       # Encoding of pixels -- channel meaning, ordering, size
                      # taken from the list of strings in include/sensor_msgs/image_encodings.h

uint8 is_bigendian    # is this data bigendian?
uint32 step           # Full row length in bytes
uint8[] data          # actual matrix data, size is (step * rows)

")



(provide :zsr/ImageBundle "c8fb7a8e02d1a79f085a43bf538d089b")


