import yaml

camera_config_file = './src/test_get_image/CameraConfigs/basler_1L.yaml'
with open(camera_config_file, 'rt') as file:
    camera_config = yaml.safe_load(file)
print(camera_config)

print(camera_config["camera_matrix"]["data"])
