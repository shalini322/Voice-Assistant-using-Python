from pyttsx3 import init

def speak(text):
    engine = init()
    engine.say(text)
    engine.runAndWait()

def open_app(app_name):
    import subprocess

    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "{Your file path}",
        "telegram": "{Your file path}",
        "file manager": "explorer.exe",  # Windows File Explorer
        "file explorer": "explorer.exe",  # Alias
        "postman": "{Your file path}",
        "excel": "{Your file path}",
        "cmd": "cmd.exe",
        "command prompt": "cmd.exe",
        "terminal": "cmd.exe"
    }

    name = app_name.lower().strip()
    command = apps.get(name)

    if command:
        try:
            subprocess.Popen(command)
            speak(f"Opening {name}")
        except Exception as e:
            speak(f"Could not open {name}")
            print(f"[ERROR] {e}")
    else:
        speak(f"App '{name}' is not recognized.")
        print(f"[ERROR] Unknown app: {name}")
