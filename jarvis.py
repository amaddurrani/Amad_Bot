import pyttsx3
import pyaudio
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')

engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("I am Amad's assistant please tell me how can i help you")

def takeComand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening. . . .")
        r.pause_threshold= 1
        audio=r.listen(source)

    try:
        print("recognizing")
        query= r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print(e)
        print("say it again please.......")
        return "None"
    return query
if __name__ == "__main__":
    wishMe()
    while True:
        query=takeComand().lower()

        if 'wikipedia' in query:
            speak('searching sir')
            query= query.replace("wikipedia","")
            results= wikipedia.summary(query,sentences=2)
            speak("searching wikipedia")
            print(results)
            speak(results)
        elif 'youtube' in query:
            webbrowser.open('youtube.com')
        elif 'google' in query:
            webbrowser.open('google.com')
        elif 'stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            print(f"sir the time is {strtime}")
            speak(f"sir the time is {strtime}")
    


