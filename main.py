Perfect sir 👏🔥 **Male Voice selected.**

Now we’ll build **Jarvis V1** in a beginner-friendly way.

# What This Version Will Do

When you run `main.py`, Jarvis can:

✅ Speak in male voice
✅ Listen from microphone
✅ Open YouTube
✅ Open Google
✅ Open Gmail
✅ Tell time
✅ Tell date
✅ Open Notepad
✅ Open Calculator
✅ Search Google
✅ Exit politely

---

# Replace Your main.py With This

```python id="ot6h2p"
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import subprocess

# ---------------------------
# Voice Engine Setup
# ---------------------------
engine = pyttsx3.init()

voices = engine.getProperty('voices')

# Try to use male voice
if len(voices) > 0:
    engine.setProperty('voice', voices[0].id)

engine.setProperty('rate', 175)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# ---------------------------
# Listen Function
# ---------------------------
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            return command

        except:
            return ""

# ---------------------------
# Command Logic
# ---------------------------
def run_jarvis():

    speak("Hello. Jarvis is ready.")

    while True:

        command = listen()

        if "youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "google" in command:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "gmail" in command:
            speak("Opening Gmail")
            webbrowser.open("https://mail.google.com")

        elif "chatgpt" in command:
            speak("Opening Chat GPT")
            webbrowser.open("https://chat.openai.com")

        elif "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            speak("Current time is " + now)

        elif "date" in command:
            today = datetime.datetime.now().strftime("%d %B %Y")
            speak("Today's date is " + today)

        elif "notepad" in command:
            speak("Opening Notepad")
            os.system("notepad")

        elif "calculator" in command:
            speak("Opening Calculator")
            subprocess.Popen("calc.exe")

        elif "search" in command:
            search_text = command.replace("search", "")
            speak("Searching " + search_text)
            webbrowser.open("https://www.google.com/search?q=" + search_text)

        elif "exit" in command or "stop" in command:
            speak("Goodbye Sir")
            break

        elif command != "":
            speak("Command not recognized")

# ---------------------------
# Start Program
# ---------------------------
run_jarvis()
```

