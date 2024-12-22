import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import wikipedia
import webbrowser
import os
import requests
import pywhatkit as kit
import imdb
import calendar


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am lyro Sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
        return query.lower()

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query

def search_on_google(query):
    kit.search(query)
def youtube(video):
    kit.playonyt(video)
def search_on_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        print(summary)
        speak(summary)
    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find any Wikipedia page matching your query. Please try a different search term.")
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]
        speak("Your query is ambiguous. Did you mean one of the following?")
        for option in options:
            speak(option)
    except Exception as e:
        speak("An error occurred while fetching the Wikipedia summary. Please try again later.")
        print(f"Error: {e}")
def get_news():
    news_headline = []
    result = requests.get(
        NEWS_FETCH_API_URL,
        params={
            "country": "in",
            "category": "general",
            "apiKey": NEWS_FETCH_API_KEY
        },
    ).json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]

def getYouTubeRecommendations():
    try:
        url = "https://www.youtube.com/feed/trending"
        webbrowser.open(url, "YouTube Trending")
    except Exception as e:
        print(e)
        speak("Sorry, I couldn't retrieve YouTube recommendations at the moment.")

def showCalendar():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    cal = calendar.month(year, month)
    speak(f"Here is the calendar for {calendar.month_name[month]} {year}.")
    print(cal)


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            search_on_wikipedia(query)

        elif 'open calculator' in query:
            path=r"C:\Users\User\OneDrive\Desktop\Calculator.lnk"
            os.startfile(path)

        elif 'open telegram' in query:
            path = r"C:\Users\User\OneDrive\Desktop\Telegram.lnk"
            os.startfile(path)

        elif 'play music' in query:
            music_dir = r'C:\Users\User\Music'
            songs = [file for file in os.listdir(music_dir) if file.endswith(('.mp3', '.wav'))]
            if songs:
                print("Available songs:", songs)
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                print("No music files found in the directory.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open notepad' in query:
            Path = "C:\\Users\\User\\OneDrive\\Desktop\\Notepad.lnk"
            os.startfile(Path)

        elif 'open whatsapp' in query:
            Path = "C:\\Users\\User\\OneDrive\\Desktop\\WhatsApp.lnk"
            os.startfile(Path)


        elif "search on google" in query:
            speak(f"What do you want to search on google")
            query = takeCommand().lower()
            search_on_google(query)

        elif "youtube" in query:
            speak("What do you want to play on youtube")
            video = takeCommand().lower()
            print(video)
            youtube(video)

        elif "recommend" in query:
            getYouTubeRecommendations()

        elif "calendar" in query:
            showCalendar()

        elif "date" in query:
            current_date = date.today()
            print("Today's date is:", current_date)
            speak(f"Today's date is: {current_date}")

        elif "news" in query:
            speak(f"I am reading out the latest headline of today")
            print(*get_news(), sep='\n')
            speak(get_news())

        elif "movie" in query:
            movies_db = imdb.IMDb()
            speak("Please tell me the movie name:")
            text = takeCommand()
            movies = movies_db.search_movie(text)
            speak("searching for" + text)
            speak("I found these")
            for movie in movies:
                title = movie["title"]
                year = movie["year"]
                speak(f"{title}-{year}")
                info = movie.getID()
                movie_info = movies_db.get_movie(info)
                rating = movie_info["rating"]
                cast = movie_info["cast"]
                actor = cast[0:5]
                plot = movie_info.get('plot outline', 'plot summary not available')
                speak(f"{title} was released in {year} has imdb ratings of {rating}.It has a cast of {actor}. "
                      f"The plot summary of movie is {plot}")

                print(f"{title} was released in {year} has imdb ratings of {rating}.\n It has a cast of {actor}. \n"
                      f"The plot summary of movie is {plot}")

        elif 'goodbye' in query:
            speak("Goodbye Sir! If you want more service do call me.")
            break




