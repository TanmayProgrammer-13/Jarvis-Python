from email.mime import audio
from unittest import result
import pyttsx3
import webbrowser
import datetime
import wikipedia
import os
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


if __name__ == "__main__":
 wish()
 while True:
  query = takeCommand().lower()

 # Logic for Jarvis
  if 'wikipedia' in query:
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)
  
  elif 'open youtube' in query:
    speak('Opening YouTube')
    webbrowser.open("youtube.com")

  elif 'open google' in query:
    speak('Opening Google')
    webbrowser.open("google.com")

  elif 'open gmail' in query:
    speak('Opening Gmail')
    webbrowser.open("gmail.com")
    
  elif 'what is the time'  in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir the Current time is {strTime}")

  elif 'open vs code' in query:
   VsCodePath = "C:\\Users\\Tanmay Sinha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
   speak("Opening Visual Studio Code")
   os.startfile(VsCodePath)

  elif 'open spotify' in query:
   Spotify = "spotify.exe"
   speak("Opening Spotify Music")
   os.startfile(Spotify)
   
  elif 'open mister programmer website' in query:
    speak('Opening mister programmer website')
    webbrowser.open("mrprogrammer.in")

  elif 'open github' in query:
    speak('Opening github')
    webbrowser.open("github.com")

  elif 'play music' in query:
   music_directory = "C:\\Music for Jarvis Program"
   songs = os.listdir(music_directory)
   print(songs)
   os.startfile(os.path.join(music_directory, songs[0]))