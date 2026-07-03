**🎛️ Volume in Air
**
A simple Python application that controls your Windows system volume using simple hand gestures and a webcam—no physical contact required! This project leverages computer vision & hand tracking to detect the distance between your thumb and index finger, allowing you to adjust the system volume in real time.

The application is built using Python, OpenCV, MediaPipe, and Pycaw, providing a smooth, intuitive, and responsive touchless volume control experience.

**Features
**
🖐️ Real-time hand detection and tracking
🎚️ Control system volume using thumb–index finger distance
📊 Live on-screen volume percentage and volume bar
🎯 Accurate hand landmark detection with MediaPipe
💻 Windows system volume integration using Pycaw
📷 Works with any standard webcam
⚡ Real-time FPS display

**🛠️ Technologies Used
**
Python 3.x
OpenCV
MediaPipe
NumPy
Pycaw
Comtypes
Webcam

**📂 Project Structure
**
Gesture-Volume-Control/
│
├── volume_control.py      # Main application
├── hand_module.py         # Hand detection module
├── requirements.txt
├── README.md


**⚙️ How It Works
**
- The webcam captures live video.
- MediaPipe detects the hand and extracts 21 hand landmarks.
- The positions of the thumb tip and index finger tip are identified.
- The Euclidean distance between these fingertips is calculated.
- The measured distance is mapped to the Windows system volume.
- Pycaw updates the system volume accordingly.

The OpenCV window displays:

- Hand landmarks
- Connecting line between fingertips
- Volume bar
- Volume percentage
- FPS counter

**🎮 Controls
**
Move thumb and index finger apart -> Increase volume
Move thumb and index finger closer -> Decrease volume
Pinch fingers together -> Minimum volume

**📋 Requirements
**
Windows 10/11
Python 3.9+ (avoid using Python 3.12+ versions)
Webcam
Speakers or headphones

**🤝 Contributing
**
Contributions, suggestions, and feature requests are welcome. Feel free to fork the repository and submit a pull request.

**📄 License
**
This project is intended for educational and learning purposes. You may modify and use it freely.
