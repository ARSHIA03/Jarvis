import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os
import smtplib
import pyaudio 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<12 :
        speak("Good Morning!")
    elif hour>= 12 and hour< 18 :
        speak("Good Afternoon!")
    else :
        speak("Good Evening!")
    speak("I am Jarvis Ma'am. How may I help you ?")

def takeCommand():
#It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = 'en-in' )
        print(f"User said : {query}\n")
     
    except Exception as e :
        #print(e)
        print("Say that again please...")
        return "None"
    return query 

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.startls()
    server.login('youremail@gmail.com','your-password-here')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #while True :
    if 1:
        query = takeCommand().lower()

        #Logic for executing tasks based on query 
        if 'wikipedia' in query :
            speak('Searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open youtube':
           webbrowser.open("youtube.com")
        
        elif 'open google':
            webbrowser.open("google.com")

        elif 'open linkedin':
            webbrowser.open("linkedin.com")

        elif 'open internshala':
            webbrowser.open("intershala.com")

        elif 'open kaggle':
            webbrowser.open("kaggle.com")

        elif 'play music' in query:
            music_dir = "D:\\Non Critical\\songs\\Favorite Songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strfttime("%H:%M:%S")

        elif 'open code' in query :
            codePath = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open powerbi' in query :
            bipath = "C:\\Program Files\\Microsoft Power BI Desktop\\bin\\PBIDesktop.exe"
            os.startfile(bipath)

        elif 'open sql' in query :
            sqlpath = "C:\\Program Files (x86)\\Microsoft SQL Server Management Studio 19\\Common7\IDE\\Ssms.exe"
            os.startfile(sqlpath)

        elif 'email to arshia' in query :
            try:
                speak("What should I say ?")
                content = takeCommand()
                to = "mathurarshia03@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e :
                print(e)
                speak("Sorry Arshia. I am unable to send this email. ")

