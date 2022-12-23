import wolframalpha
import pywhatkit as kit
import time
import wikipedia
import webbrowser
import datetime
import requests
import socket
import psutil
import platform
import math
import os
import pyttsx3
import speech_recognition as sr
from bs4 import BeautifulSoup
from plyer import notification
from colored import fg, attr

client = wolframalpha.Client("8REQUG-YQ7JGY96T8")

# Color Detection:
reset = attr('reset')
red = fg('red')
green = fg('green')
blue = fg('blue')
yellow = fg('yellow')

# Basic Details:

UserName = "Mr Khan"
BotName = "AI-Jarvis-M-2.O"

def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    lengthcode = len(Text)
    if lengthcode>30:
        engine.setProperty('rate',200)
    else:
        engine.setProperty('rate',170)
    print("    ")
    print(f"A.I : {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("    ")


def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(": Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source, 0, 8)
        try:
            print(": Recognizing.....")
            query = r.recognize_google(audio, language='en-pk')
            print(f": You Said: {query}")
        except:
            return ""
        query = str(query).lower()
        return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:
        print(yellow+f"Good Morning, Sir"+reset)
        Speak(f"Good Morning {UserName}")
    elif hour >= 12 and hour < 18:
        print(yellow+f"Good Afternoon, Sir"+reset)
        Speak(f"Good Afternoon {UserName}")
    elif hour >= 18 and hour < 24:
        print(yellow+f"Good Evening, Sir"+reset)
        Speak(f"Good Evening {UserName}")
    else:
        print(yellow+f"Good Night, Sir"+reset)
        Speak(f"Good Night {UserName}")


def StartupTime():
    strTime = datetime.datetime.now().strftime("%H")
    strTime2 = datetime.datetime.now().strftime("%M")
    strTime = int(strTime)
    strTime2 = int(strTime2)
    Speak(f"Sir, right now the time is {strTime}:{strTime2}")


def Date():
    Date = datetime.datetime.now()
    Date = Date.strftime("%d")
    Speak(f"Todays date is {Date}")


def Year():
    year = datetime.datetime.now()
    year = year.strftime("%Y")
    Speak(f"The current year is {year}")


def tellDay():
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        Speak("The day is " + day_of_the_week)


def Sweather():
    api_key = "30b2e680ad9c7790ec02fdb4f97f4573" #generate your own api key from open weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = ('peshawar')
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        r = ("outside " + " the Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
        Speak(r)
    else:
        Speak(" City Not Found ")


def Temp():
    search = "temperature in peshawar"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find('div', class_='BNeawe').text
    Speak(f"Sir the temperature in the room is {temp}")

    
def taskExe():
    
    from Features import TimeTable
##    from System import system_stats
##    from System import username
##    from System import check_int
##    from System import IPAddress
##    from System import VirtualRam
##    from System import AvailableRam
##    from System import DiskInfo
##    from System import MemoryInfo
##    from System import SysInfo
##    from System import CpuInfo

    # wishMe()
    # Date()
    # tellDay()
    # Year()
    # StartupTime()
    # system_stats()
    # username()
    # check_int()
    # Speak("Checking for your current ip address...")
    # IPAddress()
    # Sweather()
    # Speak("Checking the room temperature...")
    # Temp()
    # TimeTable()
        
    Speak("Now I am ready for your command")

    while (True):
        query = Listen()
        query = str(query)

        if len(query)<3:
            pass

        elif "translate" in query:
            from Features import Trans
            Trans()

        elif "read" in query or "a book" in query:
            from Features import Reader
            Speak("Sir which book should I read...")
            BookN = Listen()
            Reader(BookN)

        elif "generate password" in query:
            from Features import GenPass
            GenPass()
            
        elif "show my" in query:
            query = query.replace("jarvis ","")
            query = query.replace("show my ","")
            query = query.replace("password","")
            query = query.replace(" ","")
            try:
                os.startfile(rf"D:\Python\New Jarvis\DataBase\Passwords\{query}.txt")
            except FileNotFoundError as e:
                print(e)
                Speak(f"File {query} does not exist...")

        elif "crack" in query:
            from Features import PassCrack
            PassCrack()

        elif "time table" in query:
            from Features import TimeTable
            TimeTable()

        elif "todo list" in query:
            from Features import SheduleDay
            SheduleDay()

        elif "my todo" in query or "list" in query:
            Speak("For which date please mention below...")
            ddddd = input("Enter Date:- ")
            from Features import DateConverter
            dddddd = DateConverter(ddddd)
            from Features import ShowShedule
            ShowShedule(dddddd)

        elif "start writing" in query:
            from Features import Notepad
            Notepad()

        elif "close it" in query:
            from Features import CloseNotepad
            CloseNotepad()

        elif "take note" in query:
            from Features import NoteTake
            NoteTake()

        elif "reminder" in query:
            os.startfile(r"D:\Python\New Jarvis\DataBase\Reminder\Reminder.py")

        elif "instagram profile" in query:
            from Features import downInstaPro
            downInstaPro()

        elif "acronym" in query:
            from Features import Acro
            Acro()

        elif "calculate" in query:
            from Features import calculate
            query = query.replace("jarvis", "")
            query = query.replace(" calculate", "")
            query = query.replace("plus", "+")
            query = query.replace("multiply", "*")
            query = query.replace("minus", "-")
            query = query.replace("divide by", "/")
            calculate(query)

        elif "calculator" in query:
            Speak("Opening Calculator...")
            os.startfile(r"D:\Python\New Jarvis\DataBase\Gui Programs\Calculator.py")

        elif "calender" in query:
            Speak("Opening Calendar...")
            os.startfile(r"D:\Python\New Jarvis\DataBase\Gui Programs\Calendar_gui.py")

        elif "currency convertor" in query:
            Speak("Opening Currency Convertor...")
            os.startfile(r"D:\Python\New Jarvis\DataBase\Gui Programs\Currency_convertor_GUI.py")

        elif "joke" in query:
            from Features import get_random_joke
            get_random_joke()

        elif "funny joke" in query:
            from Features import tellJoke
            tellJoke()

        elif "random" in query or "advise" in query:
            from Features import get_random_advice
            get_random_advice()

        elif 'search wikipedia' in query:
            try:
                Speak('Sir, What should I search on wikipedia')
                Search = Listen()
                webbrowser.open(f"https://www.google.com/search?q={Search}")
                results = wikipedia.summary(Search, sentences=4)
                Speak("According to Wikipedia")
                Speak(results)
            except Exception as e:
                Speak("Sir I am getting information from internet...")
                time.sleep(2)
                kit.search(Search)
                try:
                    search = wikipedia.summary(Search, 2)
                    Speak(f": According To Your Search : {search}")
                except:
                    Speak("Sir I did not get what did you say but I am searching it in google...")
                    kit.search(Search)

        elif "weather update" in query:
            query = query.replace("jarvis ", "")
            query = query.replace("tell me ", "")
            query = query.replace("weather ", "")
            query = query.replace("update for ", "")
            from Features import weather_city
            weather_city(query)

        elif "tell me the weather in" in query or "tell me today's weather in" in query:
            query = query.replace("jarvis ", "")
            query = query.replace("tell me ", "")
            query = query.replace("weather in ", "")
            query = query.replace("today's ", "")
            query = query.replace("weather in ", "")
            from Features import weather_news
            weather_news(query)

        elif "fact" in query:
            from Features import RandFact
            RandFact()

        elif "activity" in query or "bore" in query:
            from Features import RandActivity
            RandActivity()

        elif "dog images" in query:
            from Features import DogImg
            DogImg()

        elif "hack" in query:
            from Features import HackRandom
            HackRandom()

        elif "set alarm" in query:
            from Features import Alarm
            Alarm(query)

        elif "this video" in query:
            from Features import DownloadYouTube
            time.sleep(2)
            DownloadYouTube()

        elif "my location" in query or "where i am" in query:
            from Internet import My_Location
            My_Location()

        elif "corona updates" in query or "corona news" in query:
            from Internet import CoronaVirus
            Speak("For which Country...")
            count = Listen()
            CoronaVirus(count)

        elif "search location" in query or "track" in query:
            query = query.replace("jarvis ","")
            query = query.replace("track ","")
            query = query.replace("search for ","")
            query = query.replace("search location ","")
            from Internet import GoogleMaps
            GoogleMaps(query)

        elif 'question' in query or "query" in query:
            Speak('tell me the question you want to get')
            question = Listen()
            Speak('getting information boss')
            try:
                try:
                    results = wikipedia.summary(question, sentences=2)
                    Speak(results)
                except:
                    client = wolframalpha.Client(client)
                    res = client.voice_data(question)
                    results = next(res.results).text
                    Speak(results)
            except:
                Speak("Sorry sir i didn't get it")
        
        elif 'how to' in query:
            import pywikihow
            Speak("Getting Data From The Internet !")
            op = query.replace("jarvis","")
            max_result = 1
            how_to_func = pywikihow.search_wikihow(op,max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            Speak(how_to_func[0].summary)

        elif "google search" in query:
            from Internet import GoogleSearch
            query = query.replace("jarvis ", "")
            query = query.replace("google search ", "")
            GoogleSearch(query)

        elif "youtube search" in query:
            from Internet import YouTubeSearch
            query = query.replace("jarvis ", "")
            query = query.replace("youtube search ", "")
            YouTubeSearch(query)

        elif "nasa news" in query:
            Speak("Tell me the date required for news extraction process...")
            date = Listen()
            from Features import DateConverter
            Con_date = DateConverter(date)
            from Nasa import NasaNews
            try:
                NasaNews(Con_date)
            except Exception as e:
                print(e)
                Speak("No speakable data found on database...")

        elif "mars images" in query:
            from Nasa import MarsImage
            try:
                MarsImage()
            except Exception as e:
                print(e)
                Speak("No speakable data found on database...")

        elif "solar bodies" in query:
            from Nasa import SolarBodies
            Speak("Sir about which solar body...")
            body = Listen()
            try:
                SolarBodies(body)
            except Exception as e:
                print(e)
                Speak("No speakable data found on database...")

        elif "astroids" in query or "near earth" in query or "astroids" in query:
            from Nasa import Astro
            from Features import DateConverter
            Speak("Tell Me The Starting Date .")
            start = input("Starting date> ")
            start_date = DateConverter(start)
            Speak("And Tell Me The End Date .")
            end = input("Ending date> ")
            end_date = DateConverter(end)
            Speak("Extracting data from nasa...")
            try:
                Astro(start_date, end_date=end_date)
            except Exception as e:
                print(e)
                Speak("No speakable data found on database...")

        elif "landpads" in query or "land pads" in query:
            from SpaceX import GetLandPadInfo
            Speak("Sir please tell me landpad id needed for extraction process...")
            iD = input("Enter the landpad id> ")
            try:
                GetLandPadInfo(iD)
            except Exception as f:
                print(e)
                Speak("No speakable data found on database...")

        elif "missions" in query:
            from SpaceX import SpaceXMission
            Speak("For which mission id you want to find information...")
            MiD = input("Enter the mission id> ")
            try:
                SpaceXMission(MiD)
            except Exception as e:
                print(e)
                Speak("No speakable data found on database...")

        elif "spacex" in query:
            from SpaceX import SpaceXInfo
            try:
                SpaceXInfo()
            except Exception as e:
                print(e)
                Speak("No speakable data found on database...")

        elif "roadster" in query:
            from SpaceX import RoadsterInfo
            try:
                RoadsterInfo()
            except Exception as e:
                print(e)
                Speak("No speakable data found on database...")

        elif "historical events" in query:
            from SpaceX import HistoricalEevents
            Speak("Sir please tell event id needed for extraction process...")
            HisId = input("Enter the event ID> ")
            try:
                HistoricalEevents(HisId)
            except Exception as e:
                print(e)
                Speak("No speakable data found on database...")

        elif "price" in query:
            query = query.replace("jarvis ", "")
            query = query.replace("tell me ", "")
            query = query.replace("tell me ", "")
            query = query.replace("current ", "")
            query = query.replace("price", "")
            query = query.replace(" of ", "")
            from Business import get_latest_crypto_price
            try:
                get_latest_crypto_price(query)
            except Exception as e:
                print(e)
                Speak("I faced some issues for fetching information...")
                Speak("It might be network issue...")

        elif "business" in query:
            from Business import BusinessNameGenerator
            query = query.replace("jarvis ", "")
            query = query.replace("tell me ", "")
            query = query.replace("a name ", "")
            query = query.replace("for my", "")
            try:
                BusinessNameGenerator(query)
            except Exception as e:
                print(e)
                Speak("I faced some issues for fetching information...")
                Speak("It might be network issue...")

        elif "price" in query or "rates" in query:
            from Business import CurrencyExchangeRates
            try:
                CurrencyExchangeRates()
            except Exception as e:
                print(e)
                Speak("I faced some issues for fetching information...")
                Speak("It might be network issue...")

        elif "free games" in query or "free game" in query:
            query = query.replace("jarvis ", "")
            query = query.replace("tell me a ", "")
            query = query.replace("free games", "")
            query = query.replace("free game", "")
            query = query.replace(" for id ", "")
            from Games import FreeToPlay
            try:
                FreeToPlay(query)
            except Exception as e:
                print(e)
                Speak("I faced some issues for fetching information...")
                Speak("It might be network issue...")

        elif "server" in query:
            from Games import MineServersInfo
            try:
                Speak("Tell me the host required for fetching information...")
                Host = input("Input host> ")
                MineServersInfo(Host)
            except Exception as e:
                print(e)
                Speak("I faced some issues for fetching information...")
                Speak("It might be network issue...")

        elif 'local disk d' in query:
            Speak("opening local disk D")
            webbrowser.open("D://")

        elif 'local disk c' in query:
            Speak("opening local disk C")
            webbrowser.open("C://")

        elif "virtual memory" in query:
            VirtualRam()
            
        elif "available memory" in query:
            AvailableRam()

        elif "system information" in query or "system details" in query:
            SysInfo()
            
        elif "cpu information" in query or "cpu details" in query:
            CpuInfo()
            
        elif "system power" in query:
            Speak("Activating system power options...")
            time.sleep(3)
            while(True):
                Speak("What do you want to do with the system...")
                OpLst = ["1.Shutdown","2.Restart","3.Sleep","4."]
                ss = Listen()


        elif "drives information" in query or "drives details" in query:
            DiskInfo()
            
        elif "memory information" in query or "memory details" in query:
            MemoryInfo()

        elif "ip address" in query:
            IPAddress()

        elif "send email" in query:
            from Internet import SendEmail
            SendEmail()
            
        elif "fetch wifi" in query or "wifi" in query or "wi-fi" in query:
            from Internet import WifiPassSender
            WifiPassSender()

        elif "new tab" in query:
            from Automation import ChromeAuto
            ChromeAuto(query)

        elif "close tab" in query:
            from Automation import ChromeAuto
            ChromeAuto(query)

        elif "new window" in query:
            from Automation import ChromeAuto
            ChromeAuto(query)

        elif "history" in query:
            from Automation import ChromeAuto
            ChromeAuto(query)

        elif "download" in query:
            from Automation import ChromeAuto
            ChromeAuto(query)

        elif "bookmark" in query:
            from Automation import ChromeAuto
            ChromeAuto(query)

        elif "incognito" in query:
            from Automation import ChromeAuto
            ChromeAuto(query)

        elif "visit" in query:
            from Automation import ChromeAuto
            ChromeAuto(query)

        elif "pause" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "resume" in query or "play" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "full screen" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "exit" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "film screen" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "skip" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "back" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "speed" in query:
            Speak("Do you want to increase or decrease")
            ply = Listen()
            if "increase" in ply:
                from Automation import YouTubeAuto
                YouTubeAuto(ply)
            elif "decrease" in ply:
                from Automation import YouTubeAuto
                YouTubeAuto(ply)
            else:
                Speak("Ok sir...")

        elif "previous" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "next" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "mute" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "unmute" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "search" in query:
            from Automation import YouTubeAuto
            YouTubeAuto(query)

        elif "home screen" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "minimize" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "show start" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "settings" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "search" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "snip" in query or "sketch" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "screenshot" in query or "screen shot" in query:
            from Automation import ScreenShot
            ScreenShot()

        elif "restore windows" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "lock" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "quick menu" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "switch window" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "virtual desktop" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "add" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "right" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "left" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "close" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif "action center" in query or "notification center" in query:
            from Automation import WindiowsAuto
            WindiowsAuto(query)

        elif 'new folder' in query:
            from Features import NewFolder
            query = query.replace("jarvis ", "")
            query = query.replace("make ", "")
            query = query.replace("new folder ", "")
            NewFolder(query)

        elif "launch" in query:
            query = query.replace("jarvis","")
            query = query.replace("launch","")
            from Automation import OpenBrowser
            OpenBrowser(query)
        
        elif "open" in query:
            query = query.replace("jarvis","")
            query = query.replace("open","")
            from Automation import OpenBrowser
            OpenBrowser(query)
        
        elif "terminate" in query or "close" in query or "application" in query:
            query = query.replace("jarvis","")
            query = query.replace("terminate","")
            query = query.replace("close","")
            query = query.replace("application","")
            from Automation import CloseApp
            CloseApp(query)

        elif "volumeup" in query or "volume up" in query:
            from Automation import volumeup
            volumeup()
        
        elif "volumedown" in query or "volume down" in query:
            from Automation import volumedown
            volumedown()

        elif "rest" in query or "sleep" in query:
            Speak("Sleep mode activated...")
            break

        else:
            from JarvisAdvancedBot.JarvisAiBrain import ReplyBrain
            Reply = ReplyBrain(query) 
            Speak(Reply)


if __name__=="__main__":
    while(True):
        query = Listen()
        if "get online" in query or "listen" in query:
            taskExe()
        
        elif "terminate" in query or "exit" in query or "quit" in query:
            break

taskExe()
