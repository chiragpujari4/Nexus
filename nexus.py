import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import os
import cmd
import cv2
import wikipedia

engine=pyttsx3.init('sapi5') #Initiating python engine.
voices=engine.getProperty('voices') #Getting voices from the engine.
engine.setProperty('voices',voices[0].id) #setting a particular voice for the model.

def speak(audio): #Function to speak.
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand(): #Function to take commands from the user.
    r=sr.Recognizer() #Speech Recognition module's recognizer.
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=4 # To pause it for listening.
        audio=r.listen(source,phrase_time_limit=5) #To listen the command.

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in') #Using Google's speech recognition model.
        print(f"user said: {query}") #To print what user said.
        speak(query)

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# Additional Functionalities -

def wish(): #Wish function
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good Morning")
    elif(hour>12 and hour<18):
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Nexus, What can I help you with")


if __name__=="__main__":
    #speak("this is nexus")
    #takecommand()
    wish()
    if 1:
        query=takecommand().lower() #Taking input from the user.
        # Tasks -
        
        if "open notepad" in query: #Open notepad.
            npath="C:\\Windows\\notepad.exe"
            os.startfile(npath)
        
        elif "open command prompt" in query:
            os.system("start cmd")            
            
        #Online Tasks -
        
        