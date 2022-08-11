import os
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices  = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour  = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Good Morning Sir!, i am jarvis, how may i help you?")

    elif hour >=12 and hour<18:
        speak("Good Afternoon Sir!, i am jarvis, how may i help you?")

    else:
        speak("Good Evening Sir!, i am jarvis, how may i help you?")


def takeCommand():
   r = sr.Recognizer()
   with sr.Microphone() as source:
    print("Listening...")
    r.pause_threshold = 1
    audio = r.listen(source)

    try:
        print("Recongizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
    #    print(e)
       print("Say that Again")
       return "None"
    return query

while True:

    wake_up = takeCommand()

    if 'wake up' in wake_up:
        os.startfile('C:\\Users\\Tanmay Sinha\\Desktop\\Voice Assitant PTTSX3\\assitant.py')
    else:
        print('Something Went Wrong...')