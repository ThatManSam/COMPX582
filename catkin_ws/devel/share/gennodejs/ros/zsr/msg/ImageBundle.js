// Auto-generated. Do not edit!

// (in-package zsr.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let sensor_msgs = _finder('sensor_msgs');
let geometry_msgs = _finder('geometry_msgs');
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class ImageBundle {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.DeviceIDs = null;
      this.LLH = null;
      this.Images = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('DeviceIDs')) {
        this.DeviceIDs = initObj.DeviceIDs
      }
      else {
        this.DeviceIDs = [];
      }
      if (initObj.hasOwnProperty('LLH')) {
        this.LLH = initObj.LLH
      }
      else {
        this.LLH = new geometry_msgs.msg.Vector3();
      }
      if (initObj.hasOwnProperty('Images')) {
        this.Images = initObj.Images
      }
      else {
        this.Images = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ImageBundle
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [DeviceIDs]
    // Serialize the length for message field [DeviceIDs]
    bufferOffset = _serializer.uint32(obj.DeviceIDs.length, buffer, bufferOffset);
    obj.DeviceIDs.forEach((val) => {
      bufferOffset = std_msgs.msg.String.serialize(val, buffer, bufferOffset);
    });
    // Serialize message field [LLH]
    bufferOffset = geometry_msgs.msg.Vector3.serialize(obj.LLH, buffer, bufferOffset);
    // Serialize message field [Images]
    // Serialize the length for message field [Images]
    bufferOffset = _serializer.uint32(obj.Images.length, buffer, bufferOffset);
    obj.Images.forEach((val) => {
      bufferOffset = sensor_msgs.msg.Image.serialize(val, buffer, bufferOffset);
    });
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ImageBundle
    let len;
    let data = new ImageBundle(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [DeviceIDs]
    // Deserialize array length for message field [DeviceIDs]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.DeviceIDs = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.DeviceIDs[i] = std_msgs.msg.String.deserialize(buffer, bufferOffset)
    }
    // Deserialize message field [LLH]
    data.LLH = geometry_msgs.msg.Vector3.deserialize(buffer, bufferOffset);
    // Deserialize message field [Images]
    // Deserialize array length for message field [Images]
    len = _deserializer.uint32(buffer, bufferOffset);
    data.Images = new Array(len);
    for (let i = 0; i < len; ++i) {
      data.Images[i] = sensor_msgs.msg.Image.deserialize(buffer, bufferOffset)
    }
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    object.DeviceIDs.forEach((val) => {
      length += std_msgs.msg.String.getMessageSize(val);
    });
    object.Images.forEach((val) => {
      length += sensor_msgs.msg.Image.getMessageSize(val);
    });
    return length + 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'zsr/ImageBundle';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c8fb7a8e02d1a79f085a43bf538d089b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    std_msgs/Header           header
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ImageBundle(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.DeviceIDs !== undefined) {
      resolved.DeviceIDs = new Array(msg.DeviceIDs.length);
      for (let i = 0; i < resolved.DeviceIDs.length; ++i) {
        resolved.DeviceIDs[i] = std_msgs.msg.String.Resolve(msg.DeviceIDs[i]);
      }
    }
    else {
      resolved.DeviceIDs = []
    }

    if (msg.LLH !== undefined) {
      resolved.LLH = geometry_msgs.msg.Vector3.Resolve(msg.LLH)
    }
    else {
      resolved.LLH = new geometry_msgs.msg.Vector3()
    }

    if (msg.Images !== undefined) {
      resolved.Images = new Array(msg.Images.length);
      for (let i = 0; i < resolved.Images.length; ++i) {
        resolved.Images[i] = sensor_msgs.msg.Image.Resolve(msg.Images[i]);
      }
    }
    else {
      resolved.Images = []
    }

    return resolved;
    }
};

module.exports = ImageBundle;
