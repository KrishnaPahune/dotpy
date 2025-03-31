import time
from plyer import notification

print("After how much time should i remind you of drinking water? ")
interval = int(input("Enter time in minutes: "))

def remind_to_drink(interval):
    while True:
        notification.notify(
            title="💧 Hydration Reminder",
            message="It's time to drink water! Stay hydrated. 🚰",
            timeout=10  # Notification disappears after 10 seconds
        )
        time.sleep(interval * 60)  # Convert minutes to seconds

# Call function with an interval of 60 minutes (1 hour)
remind_to_drink(interval)
