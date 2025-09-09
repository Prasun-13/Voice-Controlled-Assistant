import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime
import pyjokes
import wikipedia
import random


engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except:
        return ""

speak("Hello, I am your interactive Voice Assistant!")

music_folder = "C:/Users/Public/Music"

while True:
    command = listen()

    if "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}")

    elif "date" in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")

    elif "open notepad" in command:
        speak("Opening Notepad")
        os.system("notepad")

    elif "open calculator" in command:
        speak("Opening Calculator")
        os.system("calc")

    elif "google" in command:
        speak("What should I search?")
        query = listen()
        webbrowser.open(f"https://www.google.com/search?q={query}")

    elif "youtube" in command:
        speak("What should I play on YouTube?")
        query = listen()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

    elif "wikipedia" in command:
        speak("What should I search on Wikipedia?")
        query = listen()
        try:
            result = wikipedia.summary(query, sentences=2)
            speak(result)
        except:
            speak("Sorry, I couldn't fetch that.")

    elif "joke" in command:
        speak(pyjokes.get_joke())

    elif "play music" in command:
        try:
            songs = os.listdir(music_folder)
            if songs:
                song = random.choice(songs)
                speak(f"Playing {song}")
                os.startfile(os.path.join(music_folder, song))
            else:
                speak("No music files found.")
        except:
            speak("Music folder not found.")

    elif "calculate" in command:
        try:
            expression = command.replace("calculate", "").strip()
            answer = eval(expression)
            speak(f"The answer is {answer}")
        except:
            speak("Sorry, I couldn't calculate that.")

    elif "shutdown" in command:
        speak("Shutting down. Goodbye!")
        os.system("shutdown /s /t 5")
        break

    elif "exit" in command or "quit" in command:
        speak("Goodbye! Have a nice day.")
        break

    elif command.strip() != "":
        speak("I heard you say " + command + ". But I am still learning.")
 