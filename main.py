import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha

app_id = "5L4QPR-4676J2UE2G"
client = wolframalpha.Client(app_id)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning!")
    elif (hour >= 12 and hour < 18):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am EDITH Sir. Please tell me how I may help you.")


def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('gamer280904@gmail.com', 'Sept@2004')
    server.sendmail('gamer280904@gmail.com', to, content)
    server.close()


if __name__ == '__main__':
    wishme()

    while True:
        query = takecommand().lower()

        # Logic for executing
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open my channel" in query:
            webbrowser.open("https://www.youtube.com/channel/UC2_de31Ol2C1cepoKIz0gdg")

        elif 'play music' in query:
            music_dir = "D:\\Songsy"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "date" in query:
            strDate = datetime.datetime.now().date()
            print(f"The date is {strDate}")
            speak(f"Sir, the date is {strDate}")

        elif "how are you" in query:
            speak("I am good")

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif "about you" in query:
            speak("I am EDITH,a software designed by Tony Stark.My full name is Even Dead I am The Hero ")

        elif "open code" in query:
            codepath = "C:\Program Files\JetBrains\PyCharm Community Edition 2019.2.1\bin\pycharm64.exe"
            os.startfile(codepath)

        elif "exit" in query:
            speak("Goodbye")
            break

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takecommand()
                to = "subratah2004@yahoo.co.in"
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak(f"Sorry bhai...Could not send email")
