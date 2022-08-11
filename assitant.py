from email.mime import audio
from unittest import result
import pyttsx3
from bs4 import BeautifulSoup
import requests
import subprocess
import random
import smtplib
import webbrowser
import pywhatkit as kit
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
       speak('Sorry Can you say that again')
       print("Say that Again")
       return "None"
    return query

def TaskExe():
  speak('Hello Sir, I am Jarvis How can i help you')

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

  elif 'open chrome' in query:
    speak('Opening Google Chrome')
    webbrowser.open("chrome.exe")

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

  elif 'open instagram' in query:
    speak('Opening instagram')
    webbrowser.open("instagram.com")

  elif 'open twitter' in query:
   speak('Opening Twitter')
   webbrowser.open("twitter.com")

  elif 'open facebook' in query:
   speak('Opening facebook')
   webbrowser.open("facebook.com")

  elif 'play music' in query:
   music_directory = "C:\\Music for Jarvis Program"
   speak("Playing Music")
   print("Playing Music")
   songs = os.listdir(music_directory)
   print(songs)
   os.startfile(os.path.join(music_directory, songs[0]))


  elif 'great work jarvis' in query:
     speak("Thank you Sir, I Love You")

  elif 'you need a break' in query:
     speak("Ok Sir, You can Wake me up later")
     break

  elif 'how are you' in query:
     speak("I'm Fine, How are you?")

  elif 'who created you' in query:
     speak("I was created by tanmay sinha in 2022 august")

  elif 'are you better than google assistant' in query:
     speak("can't say i am just a normal artificail intellignece and google is suprerior")

  elif 'are you better than siri' in query:
     speak("Not Sure, Siri is one of my best friend")

  elif 'are you better than alexa' in query:
     speak("I Love My Dear Alexa")

  elif 'who are you' in query:
     speak("i am jarvis, a voice assistant created by mister programmer")
     
  elif 'i am fine' in query:
     speak("great! keep using me")

  elif 'i am fine' in query:
     speak("great! keep using me")

  elif 'will you marry me' in query:
     speak("probably Not, I am a Artificial Intelligence Not a Human you should marry a human being")

  elif 'you are bad' in query:
     speak("sad to hear but, i will try my best to improve")

  elif 'sing a song' in query:
    speak("Yes I can sing. I like to help you, even if it's strange. So I sing.")
  
  elif "tell me a joke" in query:
    speak("Why shouldn't you write with a broken pencil? Because it's pointless")
   
  elif "lame" in query:
    speak("Ok I Will try My Best")
# Open CMD
  elif 'open cmd' in query:
    CMD = "cmd.exe"
    speak("Opening Command Prompt")
    os.startfile(CMD)
    
# Close CMD
  elif 'close cmd' in query:
     CMD = "cmd.exe"
     speak("Closing Command Prompt")
     os.close(CMD)

  elif 'open notepad' in query:
     Notepad = "notepad.exe"
     speak("Opening Notepad")
     os.startfile(Notepad)

# Close Jarvis 
  elif 'sleep jarvis' in query:
     CMD = "cmd.exe"
     speak("Putting To Sleep, you can wake me up")
     os.close(CMD)

# temperature
  elif "temperature" in query:
    search = "temperature in patna"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text,"html.parser")
    temp = data.find("div", class_ = "BNeawe").text
    speak(f"current {search} is {temp}")
    print(f"Current Temperature In Patna {search} is {temp}")

