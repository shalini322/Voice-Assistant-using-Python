# Import necessary libraries
import cv2  # For accessing webcam and capturing images
import speech_recognition as sr  # For voice recognition (speech-to-text)
import pyttsx3  # For text-to-speech (to speak responses)
import datetime  # For generating unique filenames with timestamps
import time  # For adding delays
import os  # For file/folder management
from tkinter import Tk, Label  # For creating a simple popup GUI to show selfie
from PIL import Image, ImageTk  # For handling images in Tkinter
import threading  # To handle speaking in background to avoid freezing
from actions import open_app
import logging  # Use Python's built-in logging module to log commands

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak a message using TTS in a separate thread
def speak(text):
    def speak_now():
        engine.say(text)
        engine.runAndWait()
    # Run TTS in a separate thread so it doesn't block the main thread
    threading.Thread(target=speak_now, daemon=True).start()

# Function to listen for voice command
def listen_for_command():
    recognizer = sr.Recognizer()  # Initialize recognizer
    with sr.Microphone() as source:
        print("🎤 Say 'take my selfie' to click your picture...")
        print("🎤 Say 'open <app name>' to open any application...")  # Prompt user
        audio = recognizer.listen(source)  # Capture audio from mic

        try:
            # Convert audio to text using Google's speech API
            command = recognizer.recognize_google(audio).lower()
            print(f"✅ You said: {command}")  # Print recognized command
            return command
        except sr.UnknownValueError:
            # If the speech was not understood
            print("❌ Could not understand.")
        except sr.RequestError:
            # If there's a connection problem
            print("❌ Error connecting to recognition service.")
        return ""

# Function to capture selfie using webcam
def take_selfie():
    cam = cv2.VideoCapture(0)  # Open the default camera (webcam)

    if not cam.isOpened():
        print("❌ Cannot access webcam.")
        return

    speak("Taking your selfie in 2 seconds!")  # Announce delay
    time.sleep(2)  # Wait for 2 seconds

    ret, frame = cam.read()  # Read one frame from the webcam
    cam.release()  # Release the camera resource

    if ret:
        os.makedirs("selfies", exist_ok=True)
        # Numbered filename logic
        existing_files = os.listdir("selfies")
        existing_numbers = [
            int(f.split('_')[1].split('.')[0])
            for f in existing_files if f.startswith("selfie_") and f.endswith(".jpg") and f.split('_')[1].split('.')[0].isdigit()
        ]
        next_number = max(existing_numbers, default=0) + 1
        filename = f"selfies/selfie_{next_number}.jpg"
        cv2.imwrite(filename, frame)
        print(f"📸 Selfie saved as {filename}")
        show_image(filename)
    else:
        print("❌ Failed to take selfie.")

# Function to show the selfie in a popup window using Tkinter
def show_image(filepath):
    window = Tk()  # Create a new Tkinter window
    window.title("📸 Your Selfie")  # Set window title

    img = Image.open(filepath)  # Open the saved image
    img = img.resize((360, 250))  # Resize to fit window
    img = ImageTk.PhotoImage(img)  # Convert to format usable in Tkinter

    label = Label(window, image=img)  # Create label with image
    label.image = img  # Keep reference to avoid garbage collection
    label.pack()  # Add label to window

    window.mainloop()  # Keep the window open

# MAIN execution starts here
if __name__ == "__main__":
    # Set up logging to a file with timestamps
    logging.basicConfig(filename='voice_commands.log', level=logging.INFO, format='%(asctime)s - %(message)s')
    command = listen_for_command()
    
    if command:
        logging.info(command)  # Log every voice command with timestamp

    if "take my selfie" in command:
        take_selfie()

    elif "open" in command:
        app_name = command.replace("open", "").strip()
        if app_name:
            open_app(app_name)
        else:
            speak("Please specify an app to open.")

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I didn't understand the command.")
