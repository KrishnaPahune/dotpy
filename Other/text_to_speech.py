import win32com.client

def voice(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)

students = ["Krishna","Bhakti","Ram"]

for student in students:
    text=f"Shoutout to {student}!"
    voice(text)
    print(text)