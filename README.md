# Run the program
The program is located in `catkin_ws/src/test_get_image/src/get_image_from_ros.py`
```
catkin_ws/src/test_get_image/src/get_image_from_ros.py

Arguments
-a, --active   Enables motor output (use to demo on strawberry harvester)
-s, --size     The size of the marker (the internal square size)
-t, --target   The target distance to drive at away from the tags (only relevant if motors are engaged)
-T, --tag      The tag to turn at (only relevant if motors are engaged)
... There is more, run -h to see the full list
```

# Python virtual environment
A python virtual environment is the easiest way to ensure all the correct packages are installed.
The `requirements.txt` file contains all the needed dependencies.
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate
# Install packages
pip3 install -r requirements.txt

# Run program

# Once you are done
deactivate
```

# Stats page
Inside this file, to show the stats page (showing the distances of the detected image)
make sure that like 308 is uncommented, inside the calc_pose_opencv function
```python
show_stats(term, x, z, area)
```

# Overlay image
The current image with the overlayed tag should appear automatically.
This is opened by the `overlay_tags` function in `camera/detector.py`, which calls the `cv2.imshow(...)` to open the overlayed image

# The basler camera
For the program to find the camera, the host it is running on (like a Jetson nano) needs to be on the same subnet as the camera.
I.e., they need to be plugged into the same switch and both be allocated an IP in the same subnet, like 192.168.1.10 and 192.168.1.11.
