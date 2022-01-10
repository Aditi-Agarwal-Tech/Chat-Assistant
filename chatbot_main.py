import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import wikipedia
import webbrowser
import pyaudio
import time
from googlesearch import search
import subprocess
import wolframalpha
import requests
import urllib.request
import re

name = input("Need ur name first:")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voice_id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Hello, " + name + ". Good Morning")
        print("Hello, " + name + ". Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Hello, " + name + ". Good Afternoon")
        print("Hello, " + name + ". Good Afternoon")
    else:
        speak("Hello, " + name + ". Good Evening")
        print("Hello, " + name + ". Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(name + f":{statement}\n")

        except Exception as e:
            speak("Sorry, wasn't able to catch it.")
            return ""
        return statement


print("Loading your AI personal assistant Emma")
speak("Loading your AI personal assistant Emma")
wishMe()


def pa():
    while True:
        speak("How can I help you now?")
        statement = takeCommand().lower()
        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak('your personal assistant Emma is shutting down,Good bye')
            print('your personal assistant Emma is shutting down,Good bye')
            break
        if "thanks" in statement or "thank you" in statement:
            speak('Anytime' + name)

        if 'wikipedia' in statement:
            speak('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in statement:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("on my way")

        elif 'browser' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("here we go")

        elif 'mail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("mail time")

        elif 'news' in statement:
            webbrowser.open_new_tab("https://www.timesofindia.indiatimes.com/home/headlines")
            speak("hot headlines servin now")

        elif 'time' in statement:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            print(f"the time is {strTime}")

        elif "play" in statement or "video" in statement:
            speak("What video do you wanna play")
            query = takeCommand()
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            linkElement = "https://www.youtube.com/watch?v=" + video_ids[0]
            webbrowser.open_new_tab(linkElement)

        elif "youtube" in statement or "search video on youtube" in statement:
            speak("What do you wanna search on youtube")
            query = takeCommand()
            webbrowser.open_new_tab("https://www.youtube.com/results?search_query=" + query)

        elif 'search' in statement:
            statement = statement.replace("search", "")
            webbrowser.open_new_tab(statement)

        elif 'ask' in statement:
            speak('I can answer to computational and geographical questions  and what question do you want to ask now')
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

        elif "stackoverflow" in statement or "stack overflow" in statement:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("stackoverflow, here we go")
            print("stackoverflow, here we go")

        elif 'what could you do' in statement or 'what can you do' in statement:
            speak('I am Emma version 1.O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,search wikipedia,predict weather'
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')

        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            speak("I was built by a team of engineers")
            print("I was built by a team of engineers")

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("whats the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak(" City Not Found ")

        elif "log off" in statement or "sign out" in statement:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])
            time.sleep(3)

        elif "google" in statement:
            search("Google")
            speak("What do you wanna search")
            query = takeCommand()
            link=[]
            for j in search(query, tld="co.in", num=10, stop=10, pause=2):
                print(j)
                link.append(j)
            webbrowser.open_new_tab(link[0])
            webbrowser.open_new_tab(link[1])
            webbrowser.open_new_tab(link[2])


if __name__ == '__main__':
    speak("Hi " + name + "this is Emma")
    pa()
