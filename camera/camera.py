CAMERA_SERIAL = '23884525'


class Camera:
    def __init__(self, color=False, auto=True):
        from pypylon import pylon
        self.color = color
        self.auto_exposure = auto

        ip_address = '192.168.200.223'
        info = pylon.DeviceInfo()
        info.SetPropertyValue('IpAddress', ip_address)

        tl_factory = pylon.TlFactory.GetInstance()
        devices = tl_factory.EnumerateDevices()
        print(f"Number of devices: {len(devices)}")

        camera_device = None
        for cam in devices:
            if cam.GetSerialNumber() == CAMERA_SERIAL:
                camera_device = cam
                break

        if camera_device is None:
            raise Exception('Could not select camera')

        print(f'Selected camera {camera_device.GetModelName()} {camera_device.GetSerialNumber()}')

        self.camera = pylon.InstantCamera(tl_factory.CreateDevice(camera_device))
        self.camera.Open()
        self._configure_camera()
        new_width = self.camera.Width.GetValue() - self.camera.Width.GetInc()
        if new_width >= self.camera.Width.GetMin():
            self.camera.Width.SetValue(new_width)

        self.converter = pylon.ImageFormatConverter()
        self.converter.OutputPixelFormat = pylon.PixelType_BGR8packed
        self.converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    # def start_grabbing(self):
    #     self.camera.StartGrabbing(pylon.GrabStrategy_LatestImages)

    def _configure_camera(self):
        if self.auto_exposure:
            self.camera.ExposureAuto = 'Continuous'
            self.camera.GainAuto = 'Continuous'
        else:
            self.camera.GainAuto = 'Off'
            self.camera.GainRaw = 100
            self.camera.ExposureAuto = 'Off'
            self.camera.ExposureTimeRaw = 10000
        self.camera.BalanceWhiteAuto = 'Continuous'
        # print(self.camera.PixelFormat.Symbolics)
        self.camera.PixelFormat = 'BayerRG8' if self.color else 'Mono8'
        print(self.camera.PixelFormat.GetValue())

    def get_image(self):
        # if self.camera.IsGrabbing():
        #     grab_result = self.camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        #     if grab_result.GrabSucceeded():
        #         return self.converter.Convert(grab_result).GetArray()
        if not hasattr(self, 'camera'):
            print("Not connected to a camera, cannot get image!")
            return None
        while True:
            img = self.camera.GrabOne(5000).GetArray()
            if img.shape[0] == 0 or img.shape[1] == 0:
                print("Warning: Got invalid image, trying again")
                continue
            break
        return img

    def close_camera(self):
        if hasattr(self, 'camera') and self.camera.IsOpen():
            self.camera.Close()
        else:
            print("Warning: Tried to close camera that wasn't open, did nothing")
