; Auto-generated. Do not edit!


(cl:in-package zsr-msg)


;//! \htmlinclude ImageBundle.msg.html

(cl:defclass <ImageBundle> (roslisp-msg-protocol:ros-message)
  ((header
    :reader header
    :initarg :header
    :type std_msgs-msg:Header
    :initform (cl:make-instance 'std_msgs-msg:Header))
   (DeviceIDs
    :reader DeviceIDs
    :initarg :DeviceIDs
    :type (cl:vector std_msgs-msg:String)
   :initform (cl:make-array 0 :element-type 'std_msgs-msg:String :initial-element (cl:make-instance 'std_msgs-msg:String)))
   (LLH
    :reader LLH
    :initarg :LLH
    :type geometry_msgs-msg:Vector3
    :initform (cl:make-instance 'geometry_msgs-msg:Vector3))
   (Images
    :reader Images
    :initarg :Images
    :type (cl:vector sensor_msgs-msg:Image)
   :initform (cl:make-array 0 :element-type 'sensor_msgs-msg:Image :initial-element (cl:make-instance 'sensor_msgs-msg:Image))))
)

(cl:defclass ImageBundle (<ImageBundle>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ImageBundle>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ImageBundle)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name zsr-msg:<ImageBundle> is deprecated: use zsr-msg:ImageBundle instead.")))

(cl:ensure-generic-function 'header-val :lambda-list '(m))
(cl:defmethod header-val ((m <ImageBundle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader zsr-msg:header-val is deprecated.  Use zsr-msg:header instead.")
  (header m))

(cl:ensure-generic-function 'DeviceIDs-val :lambda-list '(m))
(cl:defmethod DeviceIDs-val ((m <ImageBundle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader zsr-msg:DeviceIDs-val is deprecated.  Use zsr-msg:DeviceIDs instead.")
  (DeviceIDs m))

(cl:ensure-generic-function 'LLH-val :lambda-list '(m))
(cl:defmethod LLH-val ((m <ImageBundle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader zsr-msg:LLH-val is deprecated.  Use zsr-msg:LLH instead.")
  (LLH m))

(cl:ensure-generic-function 'Images-val :lambda-list '(m))
(cl:defmethod Images-val ((m <ImageBundle>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader zsr-msg:Images-val is deprecated.  Use zsr-msg:Images instead.")
  (Images m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ImageBundle>) ostream)
  "Serializes a message object of type '<ImageBundle>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'header) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'DeviceIDs))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'DeviceIDs))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'LLH) ostream)
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'Images))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'Images))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ImageBundle>) istream)
  "Deserializes a message object of type '<ImageBundle>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'header) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'DeviceIDs) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'DeviceIDs)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'std_msgs-msg:String))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'LLH) istream)
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'Images) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'Images)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'sensor_msgs-msg:Image))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ImageBundle>)))
  "Returns string type for a message object of type '<ImageBundle>"
  "zsr/ImageBundle")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ImageBundle)))
  "Returns string type for a message object of type 'ImageBundle"
  "zsr/ImageBundle")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ImageBundle>)))
  "Returns md5sum for a message object of type '<ImageBundle>"
  "c8fb7a8e02d1a79f085a43bf538d089b")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ImageBundle)))
  "Returns md5sum for a message object of type 'ImageBundle"
  "c8fb7a8e02d1a79f085a43bf538d089b")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ImageBundle>)))
  "Returns full string definition for message of type '<ImageBundle>"
  (cl:format cl:nil "std_msgs/Header           header~%std_msgs/String[]        DeviceIDs~%geometry_msgs/Vector3     LLH~%sensor_msgs/Image[]      Images~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ImageBundle)))
  "Returns full string definition for message of type 'ImageBundle"
  (cl:format cl:nil "std_msgs/Header           header~%std_msgs/String[]        DeviceIDs~%geometry_msgs/Vector3     LLH~%sensor_msgs/Image[]      Images~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: sensor_msgs/Image~%# This message contains an uncompressed image~%# (0, 0) is at top-left corner of image~%#~%~%Header header        # Header timestamp should be acquisition time of image~%                     # Header frame_id should be optical frame of camera~%                     # origin of frame should be optical center of camera~%                     # +x should point to the right in the image~%                     # +y should point down in the image~%                     # +z should point into to plane of the image~%                     # If the frame_id here and the frame_id of the CameraInfo~%                     # message associated with the image conflict~%                     # the behavior is undefined~%~%uint32 height         # image height, that is, number of rows~%uint32 width          # image width, that is, number of columns~%~%# The legal values for encoding are in file src/image_encodings.cpp~%# If you want to standardize a new string format, join~%# ros-users@lists.sourceforge.net and send an email proposing a new encoding.~%~%string encoding       # Encoding of pixels -- channel meaning, ordering, size~%                      # taken from the list of strings in include/sensor_msgs/image_encodings.h~%~%uint8 is_bigendian    # is this data bigendian?~%uint32 step           # Full row length in bytes~%uint8[] data          # actual matrix data, size is (step * rows)~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ImageBundle>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'header))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'DeviceIDs) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'LLH))
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'Images) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ImageBundle>))
  "Converts a ROS message object to a list"
  (cl:list 'ImageBundle
    (cl:cons ':header (header msg))
    (cl:cons ':DeviceIDs (DeviceIDs msg))
    (cl:cons ':LLH (LLH msg))
    (cl:cons ':Images (Images msg))
))
