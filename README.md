# 🎵 AirVolume — Touchless Sound Control ✋

A real-time hand-gesture volume control system built with **MediaPipe, OpenCV, and PyCaw**. Detects hand landmarks live via webcam and dynamically maps thumb-to-index finger distance to your system's audio volume — no touching your keyboard or mouse required.

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Tasks%20API-0097A7?style=for-the-badge&logo=google&logoColor=white)
![PyCaw](https://img.shields.io/badge/PyCaw-Windows%20Audio-0078D4?style=for-the-badge&logo=windows&logoColor=white)

---

## 🚀 Features

- ✋ Real-time hand tracking
- 🖐️ 21 hand-landmark detection
- 🔇 Fully touchless volume control
- 🎚️ Smooth volume mapping
- 🪟 Direct Windows system-audio integration
- ⚡ Lightweight and fast (TensorFlow Lite backend under the hood)

---

## 🧠 How It Works

1. The webcam captures live video via OpenCV
2. MediaPipe's Hand Landmarker detects 21 hand landmarks
3. Distance is measured between:
   - **Thumb tip** (Landmark 4)
   - **Index fingertip** (Landmark 8)
4. That finger distance is mapped onto the system volume range
5. PyCaw updates the Windows master volume in real time

---

## 🎮 Controls

| Gesture / Key | Action |
|---|---|
| Spread fingers apart | Increase volume |
| Bring fingers close together | Decrease volume |
| **Q** | Exit the application |

---

## 🛠️ Tech Stack

- Python 3.10
- OpenCV
- MediaPipe Tasks API
- NumPy
- PyCaw
- Windows Core Audio API

---

## 📂 Project Structure

```
airvolume-touchless-sound-control/
│
├── volume_control.py     # Main application — hand tracking + volume mapping
├── read.py                # Helper/utility script
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

**1️⃣ Clone the repository**
```
git clone https://github.com/GouravK1107/airvolume-touchless-sound-control.git
cd airvolume-touchless-sound-control
```

**2️⃣ Create a virtual environment**
```
python -m venv venv
venv\Scripts\activate
```

**3️⃣ Install dependencies**
```
pip install -r requirements.txt
```

**4️⃣ Download the MediaPipe hand landmark model**

```
https://storage.googleapis.com/mediapipe-models/hand_landmarker/hand_landmarker/float16/latest/hand_landmarker.task
```
Place the downloaded `hand_landmarker.task` file in the project root directory.

**5️⃣ Run the project**
```
python volume_control.py
```
Press **Q** to exit.

---

## 📌 Requirements

- Windows OS (PyCaw + Core Audio API are Windows-specific)
- A webcam
- Python 3.10 recommended

---

## 💡 Future Improvements

- 📊 On-screen volume bar UI
- 🔇 Gesture-based mute toggle
- 🎚️ Smoothing filter to reduce jitter
- 👐 Multi-hand gesture recognition
- 🖥️ Cross-platform audio control (macOS/Linux support)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.
Fork → create a branch → commit → push → open a pull request.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

## 👨‍💻 Author

**Gourav R**
Backend Developer | Applied AI Developer — exploring Computer Vision & AI systems

GitHub: https://github.com/GouravK1107
Portfolio: https://gouravk1107.github.io/my-portfolio/

---

Made with ❤️ and a well-tuned pinch gesture.
