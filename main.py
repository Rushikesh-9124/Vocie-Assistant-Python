import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def talking_code():
    command = ""  # Initialize command here
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source, duration=1)  # Adjust for ambient noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
            if "sunny" in command:
                command = command.replace('sunny', '')
                print(command)
    except sr.UnknownValueError:
        print("Sorry, couldn't understand the audio.")
    except sr.RequestError:
        print("Request error, please check your internet connection.")
    return command

def run_sunny():
    command = talking_code()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print("Current time:", time)
        talk('The current time is ' + time)

run_sunny()
