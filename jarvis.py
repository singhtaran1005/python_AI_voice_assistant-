import pyttsx3  
import speech_recognition as sr  
import datetime
import wikipedia  
import webbrowser
import os
import smtplib
from email.mime import audio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon")

    else:
        speak("Good Evening") 


speak("I am Jarvis Sir. Please tell me how may I help you")

def takecommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('LISTENING')
        r.pause_threshold = 1
        audio  =  r.listen(source)
    try:
        print("Recognizing")    
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)

        print("Say that again please!")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takecommand().lower()

    #Logic for executing task based on query
    if 'wikipedia' in query:
        speak("searching wikipedia!")
        query = query.replace("Wikipedia", "")
        results = wikipedia.summary(query,sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

        
    elif 'open youtube' in query:
            webbrowser.open("youtube.com")

    elif 'open google' in query:
            webbrowser.open("google.com")

    elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com") 
    elif 'playmusic' in query:
        music_dir = 'C:\\music_dir'
        songs = os.listdir(music_dir)
        print(songs)
        os.startfile(os.path.join(music_dir,songs[0]))
        
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")
