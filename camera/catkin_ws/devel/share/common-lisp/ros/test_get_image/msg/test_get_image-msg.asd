
(cl:in-package :asdf)

(defsystem "test_get_image-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ImageBundle" :depends-on ("_package_ImageBundle"))
    (:file "_package_ImageBundle" :depends-on ("_package"))
    (:file "zsrMsg" :depends-on ("_package_zsrMsg"))
    (:file "_package_zsrMsg" :depends-on ("_package"))
  ))