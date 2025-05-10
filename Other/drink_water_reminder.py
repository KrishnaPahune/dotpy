import time
import pyttsx3
from plyer import notification

# Initialize the text-to-speech engine
engine = pyttsx3.init()

print("After how much time should i remind you of drinking water? ")
interval = int(input("Enter time in minutes: "))

def speak(message):
    engine.say(message)
    engine.runAndWait()

def remind_to_drink(interval):
    while True:
        message = "It's time to drink water! Stay hydrated. 🚰"
        notification.notify(
            title="💧 Hydration Reminder",
            message=message,
            timeout=10  # Notification disappears after 10 seconds
        )
        speak(message)
        time.sleep(interval * 60)  # Convert minutes to seconds

# Call function with an interval of 60 minutes (1 hour)
remind_to_drink(interval)
