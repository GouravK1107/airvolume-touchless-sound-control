# AirVolume – Touchless Sound Control 🎵✋

A real-time hand gesture-based volume control system built using MediaPipe, OpenCV, and PyCaw.  
This project detects hand landmarks using a machine learning model and dynamically controls system audio volume based on finger distance.

---

## 🚀 Features

- Real-time hand tracking
- 21 hand landmark detection
- Touchless volume control
- Smooth volume mapping
- Windows system audio integration
- Lightweight and fast (TensorFlow Lite backend)

---

## 🧠 How It Works

1. Webcam captures live video using OpenCV  
2. MediaPipe Hand Landmarker detects 21 hand landmarks  
3. Distance between:
   - Thumb tip (Landmark 4)
   - Index finger tip (Landmark 8)  
4. Finger distance is mapped to system volume range  
5. PyCaw updates Windows master volume in real time  

---

## 🏗️ Project Structure

```
airvolume-touchless-sound-control/
│
├── volume_control.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/GouravK1107/airvolume-touchless-sound-control.git
cd airvolume-touchless-sound-control
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 4️⃣ Download MediaPipe Model

Download the Hand Landmarker model file:

https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task

Place it in the project root directory.

### 5️⃣ Run the Project

```
python volume_control.py
```

Press **Q** to exit.

---

## 🎮 Controls

- Spread fingers → Increase volume  
- Bring fingers close → Decrease volume  
- Press Q → Exit application  

---

## 🧩 Technologies Used

- Python 3.10
- OpenCV
- MediaPipe Tasks API
- NumPy
- PyCaw
- Windows Core Audio API

---

## 💡 Future Improvements

- Add volume bar UI
- Add gesture-based mute toggle
- Add smoothing filter to reduce jitter
- Multi-hand gesture recognition
- Cross-platform audio control

---

## 📌 Requirements

- Windows OS
- Webcam
- Python 3.10 recommended

---

## 📄 License

This project is open-source and available under the MIT License.
