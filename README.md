# AI-Powered-Virtual-Mouse-using-Hand-Gestures
Control your mouse with just your hands using computer vision and AI! Move your finger to move the cursor, and click by pinching — no physical mouse needed.

![Screenshot (112)](https://github.com/user-attachments/assets/1819bfdd-4ddd-4835-959f-bdc3342a6c0b)




🚀 Features
🖐️ Hand tracking using MediaPipe + OpenCV

🖱️ Move cursor using your index finger

👆 Click by bringing index + middle fingers together

💻 Works with just a webcam — no special hardware

📦 Tech Stack
Python 3.11

OpenCV

MediaPipe

Autopy

NumPy

🛠️ Setup Instructions
Install Python 3.11
Download from: https://www.python.org/downloads/release/python-3110/

Clone this repository

bash
Copy
Edit
git clone https://github.com/yourusername/ai-virtual-mouse.git
cd ai-virtual-mouse
Create virtual environment

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # For Windows
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
If there's no requirements.txt, use:

bash
Copy
Edit
pip install opencv-python mediapipe autopy numpy
▶️ How to Run
bash
Copy
Edit
python virtual_mouse.py
Once the script starts:

Move your index finger → mouse moves

Pinch with index + middle fingers → left click

🧠 Future Add-ons (Optional Ideas)
Right-click with ring + middle finger

Scroll with palm gesture

Drag-and-drop via long pinch

Voice commands (e.g., "open browser")

📸 Requirements
A working webcam

Windows OS (recommended)

Python 3.11 (MediaPipe does not support 3.12+ as of now)

📄 License
MIT License
