import cv2
print(cv2.__version__)
print(cv2.__file__)

# Replace "/path/to/opencv" with the actual path to the OpenCV installation
cv2_path = "c:\users\smriti sah\appdata\local\programs\python\python311\lib\site-packages"

import importlib.util
spec = importlib.util.spec_from_file_location("cv2", cv2_path)
cv2 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cv2)

if hasattr(cv2, 'face'):
    print("cv2.face module is available")
else:
    print("cv2.face module is not available")
