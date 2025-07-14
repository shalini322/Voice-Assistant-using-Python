import datetime
import os

def log_command(command_text):
    # Make sure the log file exists in the same directory
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    # Log file name based on current date
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    log_path = os.path.join(log_dir, f"log_{date_str}.txt")

    # Timestamp for the entry
    time_str = datetime.datetime.now().strftime("%H:%M:%S")

    # Write to the log
    with open(log_path, "a") as f:
        f.write(f"[{time_str}] {command_text}\n")
