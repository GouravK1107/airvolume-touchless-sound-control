import cv2
import numpy as np
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

# Load model
base_options = python.BaseOptions(model_asset_path="hand_landmarker.task")

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1,
    running_mode=vision.RunningMode.IMAGE
)

detector = vision.HandLandmarker.create_from_options(options)

# Initialize PyCaw
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]

cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = detector.detect(mp_image)

    if result.hand_landmarks:
        hand_landmarks = result.hand_landmarks[0]

        h, w, _ = frame.shape

        x1 = int(hand_landmarks[4].x * w)
        y1 = int(hand_landmarks[4].y * h)

        x2 = int(hand_landmarks[8].x * w)
        y2 = int(hand_landmarks[8].y * h)

        cv2.circle(frame, (x1, y1), 10, (255, 0, 255), -1)
        cv2.circle(frame, (x2, y2), 10, (255, 0, 255), -1)
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 255), 3)

        length = np.hypot(x2 - x1, y2 - y1)

        vol = np.interp(length, [20, 200], [min_vol, max_vol])
        volume.SetMasterVolumeLevel(vol, None)

    cv2.imshow("Volume Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
