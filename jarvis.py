import pyttsx3  
import speech_recognition as sr  
import datetime
import wikipedia  
import webbrowser
import os
import smtplib
import matplotlib
import scikit-learn
from email.mime import audio
from pygame import mixer


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
        speak("Good Afternoon Sir, How are You?")

    else:
        speak("Good Evening Sir, How are You") 


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

# use smtplib to send mails from Gmail
# enable less secure apps to the account to which the email is to be sent
def sendemail(to,content):

    server = smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your_email@gmail.com','your_password')
    server.sendmail('your_email@gmail.com', to ,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takecommand().lower()

    #Logic for executing task based on query
    if 'wikipedia' in query:
        speak("searching wikipedia!, Hello")
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
        music_dir = 'C:\\music_dir\\song_name.mp3'
        #songs = os.listdir(music_dir)
        #print(songs)
        #os.startfile(os.path.join(music_dir,songs[0]))
        mixer.init()
        mixer.music.load('music_dir')
        mixer.music.play()
        
    #stop music functionality 
    elif 'stop music' in query:
            mixer.music.stop()
        
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir the time is {strTime}")

    elif 'email to Taran' in query:
        try:
                speak("What should I say?")
                content = takecommand()
                to = "your_emailgmail.com"    
                sendemail(to,content)
                speak("Email has been sent!")
        except Exception as e:
                print(e)
                speak("Sorry my friend taran bhai. I am not able to send this email")
     elif 'turn off' in query:
            speak('Good Bye Master,see ya')
            break
