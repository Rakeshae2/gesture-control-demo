Hand Gesture Recognition System 📌 Project Overview

The Hand Gesture Recognition System is an AI-based desktop automation application that enables users to control their computer using real-time hand gestures. The project uses Computer Vision and Machine Learning techniques to recognize different hand gestures through a webcam and perform predefined system actions such as opening applications, launching websites, navigating windows, and executing keyboard shortcuts.

The application is built using Python, MediaPipe, OpenCV, FastAPI, HTML, CSS, and JavaScript. FastAPI provides a web interface where users can start or stop gesture recognition and view usage instructions.

Features Real-time hand gesture recognition FastAPI-based web interface Webcam-based gesture detection Open Google using gesture Open YouTube using gesture Launch Notepad Launch Calculator Open File Explorer Browser Back shortcut Show Desktop shortcut Close active window Start and Stop gesture recognition from the web interface User instruction page Responsive frontend Technologies Used Frontend HTML5 CSS3 JavaScript Backend FastAPI Python Computer Vision OpenCV MediaPipe Automation PyAutoGUI WebBrowser Subprocess Other Libraries SpeechRecognition Deep Translator System Requirements Software Python 3.10 or above Visual Studio Code FastAPI Uvicorn Hardware Webcam Windows Operating System Minimum 4 GB RAM Intel i3 Processor or above Installation Clone the repository git clone https://github.com/yourusername/hand-gesture-recognition.git

cd hand-gesture-recognition Create Virtual Environment

Windows

python -m venv .venv

Activate

.venv\Scripts\activate Install Dependencies pip install -r requirements.txt

or

pip install fastapi uvicorn opencv-python mediapipe pyautogui SpeechRecognition deep-translator Run the Project

Start the FastAPI server

python -m uvicorn app:app --reload

Open the browser

http://127.0.0.1:8000

Click

Start Gesture Recognition

Allow webcam permission.

Perform gestures in front of the webcam.

Project Structure gesture/ │ ├── app.py ├── gesture.py │ ├── templates/ │ ├── index.html │ └── instructions.html │ ├── static/ │ ├── css/ │ │ └── style.css │ └── js/ │ └── script.js │ ├── requirements.txt └── README.md Supported Gestures Gesture Action 👍 Thumbs Up Open Google 🖐 Open Palm Open YouTube ☝ One Finger Open Notepad 🤟 Three Fingers Open Calculator ✋ Four Fingers Open File Explorer 🤘 Index + Pinky Browser Back 🤙 Thumb + Pinky Close Active Window 🖕 Middle Finger Show Desktop ☝ Little Finger Disable Control Mode Working Process The webcam captures live video. OpenCV processes each video frame. MediaPipe detects the user's hand landmarks. The system identifies which fingers are raised. The detected gesture is matched with predefined commands. The corresponding system action is executed. The detected gesture is displayed on the camera screen. Advantages Contactless computer control User-friendly interface Real-time gesture recognition Fast and lightweight Improves accessibility Easy to extend with new gestures Beginner-friendly implementation Limitations Supports only one hand at a time. Requires good lighting conditions. Designed for Windows operating systems. Gesture accuracy may decrease with improper hand positioning. Requires a webcam. Future Enhancements Voice command integration Custom gesture training Multi-hand gesture recognition Cross-platform support (Windows, Linux, macOS) AI-based personalized gestures Smart home and IoT device control Gesture logging and analytics Mobile application support Important Note

This application is intended to run locally on the user's computer because it performs operating system automation (opening applications, keyboard shortcuts, and desktop control). While the FastAPI web interface can be accessed through a browser, the gesture recognition and automation features require local access to the webcam and operating system. These features cannot function correctly when deployed to a remote web server.

Author

Rakesh Kudipudi

B.Tech – Computer Science and Engineering

Python | FastAPI | Computer Vision | AI | Machine Learning | Web Development
