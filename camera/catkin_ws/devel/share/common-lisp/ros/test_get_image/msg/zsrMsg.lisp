; Auto-generated. Do not edit!


(cl:in-package test_get_image-msg)


;//! \htmlinclude zsrMsg.msg.html

(cl:defclass <zsrMsg> (roslisp-msg-protocol:ros-message)
  ((utcTime
    :reader utcTime
    :initarg :utcTime
    :type cl:float
    :initform 0.0)
   (latitude
    :reader latitude
    :initarg :latitude
    :type cl:float
    :initform 0.0)
   (longitude
    :reader longitude
    :initarg :longitude
    :type cl:float
    :initform 0.0)
   (altitude
    :reader altitude
    :initarg :altitude
    :type cl:float
    :initform 0.0)
   (heading
    :reader heading
    :initarg :heading
    :type cl:float
    :initform 0.0)
   (propertyType
    :reader propertyType
    :initarg :propertyType
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (measure
    :reader measure
    :initarg :measure
    :type cl:float
    :initform 0.0)
   (feature
    :reader feature
    :initarg :feature
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (process
    :reader process
    :initarg :process
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (parameter
    :reader parameter
    :initarg :parameter
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (resultQuality
    :reader resultQuality
    :initarg :resultQuality
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (OrchardID
    :reader OrchardID
    :initarg :OrchardID
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (CameraID
    :reader CameraID
    :initarg :CameraID
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (SecondaryCameraID
    :reader SecondaryCameraID
    :initarg :SecondaryCameraID
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (ImageID
    :reader ImageID
    :initarg :ImageID
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (SecondaryImageID
    :reader SecondaryImageID
    :initarg :SecondaryImageID
    :type std_msgs-msg:String
    :initform (cl:make-instance 'std_msgs-msg:String))
   (INSlatitude
    :reader INSlatitude
    :initarg :INSlatitude
    :type cl:float
    :initform 0.0)
   (INSlongitude
    :reader INSlongitude
    :initarg :INSlongitude
    :type cl:float
    :initform 0.0)
   (INSaltitude
    :reader INSaltitude
    :initarg :INSaltitude
    :type cl:float
    :initform 0.0)
   (INStime
    :reader INStime
    :initarg :INStime
    :type cl:float
    :initform 0.0))
)

(cl:defclass zsrMsg (<zsrMsg>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <zsrMsg>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'zsrMsg)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name test_get_image-msg:<zsrMsg> is deprecated: use test_get_image-msg:zsrMsg instead.")))

(cl:ensure-generic-function 'utcTime-val :lambda-list '(m))
(cl:defmethod utcTime-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:utcTime-val is deprecated.  Use test_get_image-msg:utcTime instead.")
  (utcTime m))

(cl:ensure-generic-function 'latitude-val :lambda-list '(m))
(cl:defmethod latitude-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:latitude-val is deprecated.  Use test_get_image-msg:latitude instead.")
  (latitude m))

(cl:ensure-generic-function 'longitude-val :lambda-list '(m))
(cl:defmethod longitude-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:longitude-val is deprecated.  Use test_get_image-msg:longitude instead.")
  (longitude m))

(cl:ensure-generic-function 'altitude-val :lambda-list '(m))
(cl:defmethod altitude-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:altitude-val is deprecated.  Use test_get_image-msg:altitude instead.")
  (altitude m))

(cl:ensure-generic-function 'heading-val :lambda-list '(m))
(cl:defmethod heading-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:heading-val is deprecated.  Use test_get_image-msg:heading instead.")
  (heading m))

(cl:ensure-generic-function 'propertyType-val :lambda-list '(m))
(cl:defmethod propertyType-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:propertyType-val is deprecated.  Use test_get_image-msg:propertyType instead.")
  (propertyType m))

(cl:ensure-generic-function 'measure-val :lambda-list '(m))
(cl:defmethod measure-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:measure-val is deprecated.  Use test_get_image-msg:measure instead.")
  (measure m))

(cl:ensure-generic-function 'feature-val :lambda-list '(m))
(cl:defmethod feature-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:feature-val is deprecated.  Use test_get_image-msg:feature instead.")
  (feature m))

(cl:ensure-generic-function 'process-val :lambda-list '(m))
(cl:defmethod process-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:process-val is deprecated.  Use test_get_image-msg:process instead.")
  (process m))

(cl:ensure-generic-function 'parameter-val :lambda-list '(m))
(cl:defmethod parameter-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:parameter-val is deprecated.  Use test_get_image-msg:parameter instead.")
  (parameter m))

(cl:ensure-generic-function 'resultQuality-val :lambda-list '(m))
(cl:defmethod resultQuality-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:resultQuality-val is deprecated.  Use test_get_image-msg:resultQuality instead.")
  (resultQuality m))

(cl:ensure-generic-function 'OrchardID-val :lambda-list '(m))
(cl:defmethod OrchardID-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:OrchardID-val is deprecated.  Use test_get_image-msg:OrchardID instead.")
  (OrchardID m))

(cl:ensure-generic-function 'CameraID-val :lambda-list '(m))
(cl:defmethod CameraID-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:CameraID-val is deprecated.  Use test_get_image-msg:CameraID instead.")
  (CameraID m))

(cl:ensure-generic-function 'SecondaryCameraID-val :lambda-list '(m))
(cl:defmethod SecondaryCameraID-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:SecondaryCameraID-val is deprecated.  Use test_get_image-msg:SecondaryCameraID instead.")
  (SecondaryCameraID m))

(cl:ensure-generic-function 'ImageID-val :lambda-list '(m))
(cl:defmethod ImageID-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:ImageID-val is deprecated.  Use test_get_image-msg:ImageID instead.")
  (ImageID m))

(cl:ensure-generic-function 'SecondaryImageID-val :lambda-list '(m))
(cl:defmethod SecondaryImageID-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:SecondaryImageID-val is deprecated.  Use test_get_image-msg:SecondaryImageID instead.")
  (SecondaryImageID m))

(cl:ensure-generic-function 'INSlatitude-val :lambda-list '(m))
(cl:defmethod INSlatitude-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:INSlatitude-val is deprecated.  Use test_get_image-msg:INSlatitude instead.")
  (INSlatitude m))

(cl:ensure-generic-function 'INSlongitude-val :lambda-list '(m))
(cl:defmethod INSlongitude-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:INSlongitude-val is deprecated.  Use test_get_image-msg:INSlongitude instead.")
  (INSlongitude m))

(cl:ensure-generic-function 'INSaltitude-val :lambda-list '(m))
(cl:defmethod INSaltitude-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:INSaltitude-val is deprecated.  Use test_get_image-msg:INSaltitude instead.")
  (INSaltitude m))

(cl:ensure-generic-function 'INStime-val :lambda-list '(m))
(cl:defmethod INStime-val ((m <zsrMsg>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader test_get_image-msg:INStime-val is deprecated.  Use test_get_image-msg:INStime instead.")
  (INStime m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <zsrMsg>) ostream)
  "Serializes a message object of type '<zsrMsg>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'utcTime))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'latitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'longitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'altitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'heading))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'propertyType) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'measure))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'feature) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'process) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'parameter) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'resultQuality) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'OrchardID) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'CameraID) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'SecondaryCameraID) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'ImageID) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'SecondaryImageID) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'INSlatitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'INSlongitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'INSaltitude))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'INStime))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <zsrMsg>) istream)
  "Deserializes a message object of type '<zsrMsg>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'utcTime) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'latitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'longitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'altitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'heading) (roslisp-utils:decode-double-float-bits bits)))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'propertyType) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'measure) (roslisp-utils:decode-double-float-bits bits)))
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'feature) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'process) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'parameter) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'resultQuality) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'OrchardID) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'CameraID) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'SecondaryCameraID) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'ImageID) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'SecondaryImageID) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'INSlatitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'INSlongitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'INSaltitude) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'INStime) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<zsrMsg>)))
  "Returns string type for a message object of type '<zsrMsg>"
  "test_get_image/zsrMsg")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'zsrMsg)))
  "Returns string type for a message object of type 'zsrMsg"
  "test_get_image/zsrMsg")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<zsrMsg>)))
  "Returns md5sum for a message object of type '<zsrMsg>"
  "8acb67a9b0a2fd36aee93ed2e2fde2cc")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'zsrMsg)))
  "Returns md5sum for a message object of type 'zsrMsg"
  "8acb67a9b0a2fd36aee93ed2e2fde2cc")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<zsrMsg>)))
  "Returns full string definition for message of type '<zsrMsg>"
  (cl:format cl:nil "float64             utcTime~%float64             latitude~%float64             longitude~%float64             altitude~%float64             heading~%~%std_msgs/String     propertyType~%float64             measure~%~%std_msgs/String     feature~%std_msgs/String     process~%std_msgs/String     parameter~%std_msgs/String     resultQuality~%~%std_msgs/String     OrchardID~%std_msgs/String     CameraID~%std_msgs/String     SecondaryCameraID~%std_msgs/String     ImageID~%std_msgs/String     SecondaryImageID~%~%float64             INSlatitude~%float64             INSlongitude~%float64             INSaltitude~%float64             INStime~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'zsrMsg)))
  "Returns full string definition for message of type 'zsrMsg"
  (cl:format cl:nil "float64             utcTime~%float64             latitude~%float64             longitude~%float64             altitude~%float64             heading~%~%std_msgs/String     propertyType~%float64             measure~%~%std_msgs/String     feature~%std_msgs/String     process~%std_msgs/String     parameter~%std_msgs/String     resultQuality~%~%std_msgs/String     OrchardID~%std_msgs/String     CameraID~%std_msgs/String     SecondaryCameraID~%std_msgs/String     ImageID~%std_msgs/String     SecondaryImageID~%~%float64             INSlatitude~%float64             INSlongitude~%float64             INSaltitude~%float64             INStime~%~%================================================================================~%MSG: std_msgs/String~%string data~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <zsrMsg>))
  (cl:+ 0
     8
     8
     8
     8
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'propertyType))
     8
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'feature))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'process))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'parameter))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'resultQuality))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'OrchardID))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'CameraID))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'SecondaryCameraID))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'ImageID))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'SecondaryImageID))
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <zsrMsg>))
  "Converts a ROS message object to a list"
  (cl:list 'zsrMsg
    (cl:cons ':utcTime (utcTime msg))
    (cl:cons ':latitude (latitude msg))
    (cl:cons ':longitude (longitude msg))
    (cl:cons ':altitude (altitude msg))
    (cl:cons ':heading (heading msg))
    (cl:cons ':propertyType (propertyType msg))
    (cl:cons ':measure (measure msg))
    (cl:cons ':feature (feature msg))
    (cl:cons ':process (process msg))
    (cl:cons ':parameter (parameter msg))
    (cl:cons ':resultQuality (resultQuality msg))
    (cl:cons ':OrchardID (OrchardID msg))
    (cl:cons ':CameraID (CameraID msg))
    (cl:cons ':SecondaryCameraID (SecondaryCameraID msg))
    (cl:cons ':ImageID (ImageID msg))
    (cl:cons ':SecondaryImageID (SecondaryImageID msg))
    (cl:cons ':INSlatitude (INSlatitude msg))
    (cl:cons ':INSlongitude (INSlongitude msg))
    (cl:cons ':INSaltitude (INSaltitude msg))
    (cl:cons ':INStime (INStime msg))
))
