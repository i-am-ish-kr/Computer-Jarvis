import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
#import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Amish")
    
    elif hour>=12 and hour<17:
        speak("Good Afternoon Amish")

    else:
        speak("Good Evening Amish")

    speak("I am Jarvis Sir. Please tell me how may I help you.")


def takeCommand():
    #it take commands from microphone and converts its to string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Sir...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


#def sendEmail(to, content):
#    server = smtplib.SMTP('smtp.gmail.com', 587)
#    server.ehlo()
#    server.starttls()
#    server.login('youremail@gmail.com', 'your-password')
#    server.sendmail('youremail@gmail.com', to, content)
#    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open geeksforgeeks' in query:
            webbrowser.open("geeksforgeeks.org")   
        
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")   
        
        elif 'open accenture' in query:
            webbrowser.open("accenturelearning.tekstac.com/login/index.php")   
        
        elif 'open learnmall' in query:
            webbrowser.open("learnmall.in")
        
        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open code' in query:
            codePath = "C:\\Users\\AMISH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = "F:\\songs"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

#        elif 'email to Amish' in query:
#            try:
#                speak("What should I say?")
#                content = takeCommand()
#                to = "harryyourEmail@gmail.com"    
#                sendEmail(to, content)
#                speak("Email has been sent!")
#            except Exception as e:
#                print(e)
#                speak("Sorry my friend harry bhai. I am not able to send this email")    

    
        elif 'quit' in query or 'bye' in query:
            speak("Quitting Sir, See you Soon, Good Bye!")
            exit()