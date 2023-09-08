// Auto-generated. Do not edit!

// (in-package zsr.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class zsrMsg {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.utcTime = null;
      this.latitude = null;
      this.longitude = null;
      this.altitude = null;
      this.heading = null;
      this.propertyType = null;
      this.measure = null;
      this.feature = null;
      this.process = null;
      this.parameter = null;
      this.resultQuality = null;
      this.OrchardID = null;
      this.CameraID = null;
      this.SecondaryCameraID = null;
      this.ImageID = null;
      this.SecondaryImageID = null;
      this.INSlatitude = null;
      this.INSlongitude = null;
      this.INSaltitude = null;
      this.INStime = null;
    }
    else {
      if (initObj.hasOwnProperty('utcTime')) {
        this.utcTime = initObj.utcTime
      }
      else {
        this.utcTime = 0.0;
      }
      if (initObj.hasOwnProperty('latitude')) {
        this.latitude = initObj.latitude
      }
      else {
        this.latitude = 0.0;
      }
      if (initObj.hasOwnProperty('longitude')) {
        this.longitude = initObj.longitude
      }
      else {
        this.longitude = 0.0;
      }
      if (initObj.hasOwnProperty('altitude')) {
        this.altitude = initObj.altitude
      }
      else {
        this.altitude = 0.0;
      }
      if (initObj.hasOwnProperty('heading')) {
        this.heading = initObj.heading
      }
      else {
        this.heading = 0.0;
      }
      if (initObj.hasOwnProperty('propertyType')) {
        this.propertyType = initObj.propertyType
      }
      else {
        this.propertyType = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('measure')) {
        this.measure = initObj.measure
      }
      else {
        this.measure = 0.0;
      }
      if (initObj.hasOwnProperty('feature')) {
        this.feature = initObj.feature
      }
      else {
        this.feature = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('process')) {
        this.process = initObj.process
      }
      else {
        this.process = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('parameter')) {
        this.parameter = initObj.parameter
      }
      else {
        this.parameter = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('resultQuality')) {
        this.resultQuality = initObj.resultQuality
      }
      else {
        this.resultQuality = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('OrchardID')) {
        this.OrchardID = initObj.OrchardID
      }
      else {
        this.OrchardID = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('CameraID')) {
        this.CameraID = initObj.CameraID
      }
      else {
        this.CameraID = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('SecondaryCameraID')) {
        this.SecondaryCameraID = initObj.SecondaryCameraID
      }
      else {
        this.SecondaryCameraID = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('ImageID')) {
        this.ImageID = initObj.ImageID
      }
      else {
        this.ImageID = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('SecondaryImageID')) {
        this.SecondaryImageID = initObj.SecondaryImageID
      }
      else {
        this.SecondaryImageID = new std_msgs.msg.String();
      }
      if (initObj.hasOwnProperty('INSlatitude')) {
        this.INSlatitude = initObj.INSlatitude
      }
      else {
        this.INSlatitude = 0.0;
      }
      if (initObj.hasOwnProperty('INSlongitude')) {
        this.INSlongitude = initObj.INSlongitude
      }
      else {
        this.INSlongitude = 0.0;
      }
      if (initObj.hasOwnProperty('INSaltitude')) {
        this.INSaltitude = initObj.INSaltitude
      }
      else {
        this.INSaltitude = 0.0;
      }
      if (initObj.hasOwnProperty('INStime')) {
        this.INStime = initObj.INStime
      }
      else {
        this.INStime = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type zsrMsg
    // Serialize message field [utcTime]
    bufferOffset = _serializer.float64(obj.utcTime, buffer, bufferOffset);
    // Serialize message field [latitude]
    bufferOffset = _serializer.float64(obj.latitude, buffer, bufferOffset);
    // Serialize message field [longitude]
    bufferOffset = _serializer.float64(obj.longitude, buffer, bufferOffset);
    // Serialize message field [altitude]
    bufferOffset = _serializer.float64(obj.altitude, buffer, bufferOffset);
    // Serialize message field [heading]
    bufferOffset = _serializer.float64(obj.heading, buffer, bufferOffset);
    // Serialize message field [propertyType]
    bufferOffset = std_msgs.msg.String.serialize(obj.propertyType, buffer, bufferOffset);
    // Serialize message field [measure]
    bufferOffset = _serializer.float64(obj.measure, buffer, bufferOffset);
    // Serialize message field [feature]
    bufferOffset = std_msgs.msg.String.serialize(obj.feature, buffer, bufferOffset);
    // Serialize message field [process]
    bufferOffset = std_msgs.msg.String.serialize(obj.process, buffer, bufferOffset);
    // Serialize message field [parameter]
    bufferOffset = std_msgs.msg.String.serialize(obj.parameter, buffer, bufferOffset);
    // Serialize message field [resultQuality]
    bufferOffset = std_msgs.msg.String.serialize(obj.resultQuality, buffer, bufferOffset);
    // Serialize message field [OrchardID]
    bufferOffset = std_msgs.msg.String.serialize(obj.OrchardID, buffer, bufferOffset);
    // Serialize message field [CameraID]
    bufferOffset = std_msgs.msg.String.serialize(obj.CameraID, buffer, bufferOffset);
    // Serialize message field [SecondaryCameraID]
    bufferOffset = std_msgs.msg.String.serialize(obj.SecondaryCameraID, buffer, bufferOffset);
    // Serialize message field [ImageID]
    bufferOffset = std_msgs.msg.String.serialize(obj.ImageID, buffer, bufferOffset);
    // Serialize message field [SecondaryImageID]
    bufferOffset = std_msgs.msg.String.serialize(obj.SecondaryImageID, buffer, bufferOffset);
    // Serialize message field [INSlatitude]
    bufferOffset = _serializer.float64(obj.INSlatitude, buffer, bufferOffset);
    // Serialize message field [INSlongitude]
    bufferOffset = _serializer.float64(obj.INSlongitude, buffer, bufferOffset);
    // Serialize message field [INSaltitude]
    bufferOffset = _serializer.float64(obj.INSaltitude, buffer, bufferOffset);
    // Serialize message field [INStime]
    bufferOffset = _serializer.float64(obj.INStime, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type zsrMsg
    let len;
    let data = new zsrMsg(null);
    // Deserialize message field [utcTime]
    data.utcTime = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [latitude]
    data.latitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [longitude]
    data.longitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [altitude]
    data.altitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [heading]
    data.heading = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [propertyType]
    data.propertyType = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [measure]
    data.measure = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [feature]
    data.feature = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [process]
    data.process = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [parameter]
    data.parameter = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [resultQuality]
    data.resultQuality = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [OrchardID]
    data.OrchardID = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [CameraID]
    data.CameraID = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [SecondaryCameraID]
    data.SecondaryCameraID = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [ImageID]
    data.ImageID = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [SecondaryImageID]
    data.SecondaryImageID = std_msgs.msg.String.deserialize(buffer, bufferOffset);
    // Deserialize message field [INSlatitude]
    data.INSlatitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [INSlongitude]
    data.INSlongitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [INSaltitude]
    data.INSaltitude = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [INStime]
    data.INStime = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.String.getMessageSize(object.propertyType);
    length += std_msgs.msg.String.getMessageSize(object.feature);
    length += std_msgs.msg.String.getMessageSize(object.process);
    length += std_msgs.msg.String.getMessageSize(object.parameter);
    length += std_msgs.msg.String.getMessageSize(object.resultQuality);
    length += std_msgs.msg.String.getMessageSize(object.OrchardID);
    length += std_msgs.msg.String.getMessageSize(object.CameraID);
    length += std_msgs.msg.String.getMessageSize(object.SecondaryCameraID);
    length += std_msgs.msg.String.getMessageSize(object.ImageID);
    length += std_msgs.msg.String.getMessageSize(object.SecondaryImageID);
    return length + 80;
  }

  static datatype() {
    // Returns string type for a message object
    return 'zsr/zsrMsg';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8acb67a9b0a2fd36aee93ed2e2fde2cc';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64             utcTime
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new zsrMsg(null);
    if (msg.utcTime !== undefined) {
      resolved.utcTime = msg.utcTime;
    }
    else {
      resolved.utcTime = 0.0
    }

    if (msg.latitude !== undefined) {
      resolved.latitude = msg.latitude;
    }
    else {
      resolved.latitude = 0.0
    }

    if (msg.longitude !== undefined) {
      resolved.longitude = msg.longitude;
    }
    else {
      resolved.longitude = 0.0
    }

    if (msg.altitude !== undefined) {
      resolved.altitude = msg.altitude;
    }
    else {
      resolved.altitude = 0.0
    }

    if (msg.heading !== undefined) {
      resolved.heading = msg.heading;
    }
    else {
      resolved.heading = 0.0
    }

    if (msg.propertyType !== undefined) {
      resolved.propertyType = std_msgs.msg.String.Resolve(msg.propertyType)
    }
    else {
      resolved.propertyType = new std_msgs.msg.String()
    }

    if (msg.measure !== undefined) {
      resolved.measure = msg.measure;
    }
    else {
      resolved.measure = 0.0
    }

    if (msg.feature !== undefined) {
      resolved.feature = std_msgs.msg.String.Resolve(msg.feature)
    }
    else {
      resolved.feature = new std_msgs.msg.String()
    }

    if (msg.process !== undefined) {
      resolved.process = std_msgs.msg.String.Resolve(msg.process)
    }
    else {
      resolved.process = new std_msgs.msg.String()
    }

    if (msg.parameter !== undefined) {
      resolved.parameter = std_msgs.msg.String.Resolve(msg.parameter)
    }
    else {
      resolved.parameter = new std_msgs.msg.String()
    }

    if (msg.resultQuality !== undefined) {
      resolved.resultQuality = std_msgs.msg.String.Resolve(msg.resultQuality)
    }
    else {
      resolved.resultQuality = new std_msgs.msg.String()
    }

    if (msg.OrchardID !== undefined) {
      resolved.OrchardID = std_msgs.msg.String.Resolve(msg.OrchardID)
    }
    else {
      resolved.OrchardID = new std_msgs.msg.String()
    }

    if (msg.CameraID !== undefined) {
      resolved.CameraID = std_msgs.msg.String.Resolve(msg.CameraID)
    }
    else {
      resolved.CameraID = new std_msgs.msg.String()
    }

    if (msg.SecondaryCameraID !== undefined) {
      resolved.SecondaryCameraID = std_msgs.msg.String.Resolve(msg.SecondaryCameraID)
    }
    else {
      resolved.SecondaryCameraID = new std_msgs.msg.String()
    }

    if (msg.ImageID !== undefined) {
      resolved.ImageID = std_msgs.msg.String.Resolve(msg.ImageID)
    }
    else {
      resolved.ImageID = new std_msgs.msg.String()
    }

    if (msg.SecondaryImageID !== undefined) {
      resolved.SecondaryImageID = std_msgs.msg.String.Resolve(msg.SecondaryImageID)
    }
    else {
      resolved.SecondaryImageID = new std_msgs.msg.String()
    }

    if (msg.INSlatitude !== undefined) {
      resolved.INSlatitude = msg.INSlatitude;
    }
    else {
      resolved.INSlatitude = 0.0
    }

    if (msg.INSlongitude !== undefined) {
      resolved.INSlongitude = msg.INSlongitude;
    }
    else {
      resolved.INSlongitude = 0.0
    }

    if (msg.INSaltitude !== undefined) {
      resolved.INSaltitude = msg.INSaltitude;
    }
    else {
      resolved.INSaltitude = 0.0
    }

    if (msg.INStime !== undefined) {
      resolved.INStime = msg.INStime;
    }
    else {
      resolved.INStime = 0.0
    }

    return resolved;
    }
};

module.exports = zsrMsg;
