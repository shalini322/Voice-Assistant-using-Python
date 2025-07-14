# 🎙️ Voice-Controlled Assistant in Python

A voice-enabled desktop assistant built with Python that responds to natural voice commands like **"take my selfie"**, **"open notepad"**, or **"open WhatsApp"**, and performs real actions such as taking a photo using your webcam, opening applications, and logging commands.

---

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
├── app.py # Main program logic
├── actions.py # Handles opening apps
├── logs/ # Command logs stored by date
│ └── log_YYYY-MM-DD.txt
├── selfies/ # Saved selfies (numbered automatically)
│ └── selfie_N.jpg
├── README.md

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
