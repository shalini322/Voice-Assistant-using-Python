# 🎙️ Voice-Controlled Assistant in Python

A voice-enabled desktop assistant built with Python that responds to natural voice commands like **"take my selfie"**, **"open notepad"**, or **"open WhatsApp"**, and performs real actions such as taking a photo using your webcam, opening applications, and logging commands.

🧪 _This was my first attempt at testing various Python libraries like `speech_recognition`, `pyttsx3`, `opencv-python`, and more to build a practical, interactive project._  
It helped me understand how voice interfaces and real-world automation can work together using simple logic and external packages.

---

Watch Demo video here : https://drive.google.com/file/d/1sF1exrBDbFEfHX9VoryTo3Bvu6UHyxaz/view?usp=sharing
(Turn up your volume while watching. The applications didn't show in the recording due to security purposes of the system but it works fine.) 

## 🚀 Features

- 🎤 Voice command recognition using your microphone
- 📸 Take a selfie using your webcam and view it instantly
- 🗂️ Open applications like Chrome, WhatsApp, Notepad, and more
- 🧾 Maintains a log of all commands with date and time
- 🖼️ Pops up your captured image using Tkinter GUI

---

## 🛠️ Technologies Used

- `speech_recognition` – for speech-to-text
- `pyttsx3` – for text-to-speech
- `opencv-python` – for webcam access and image capture
- `pillow` – to display images in Tkinter
- `tkinter` – for simple GUI popup
- `subprocess` and `os` – for application launching

---

## 📂 Folder Structure

voice-assistant/

├── app.py           # Main program logic

├── actions.py       # Handles opening apps

├── logs/            # Command logs stored by date

│   └── log_YYYY-MM-DD.txt

├── selfies/         # Saved selfies (numbered automatically)

│   └── selfie_N.jpg

├── README.md        # Project documentation


---

## 💻 Installation

### 1. Clone the repository

```bash
git clone https://github.com/shalini322/Voice-Assistant-using-Python.git
cd Voice-Assistant-using-Python
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the file

```bash
python app.py
```
