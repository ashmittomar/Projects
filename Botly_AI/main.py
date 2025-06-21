import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyjokes
import pywhatkit

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, I can't access the service right now.")
        return ""

def perform_task(command):
    if "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak(f"The current time is {time}")

    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif "joke" in command:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "exit" in command or "quit" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I can't do that yet.")

speak("Hello! I am your assistant Botly. How can I help you?")
while True:
    user_command = listen()
    if user_command:
        perform_task(user_command)
