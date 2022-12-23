import string
import random
import PyPDF2
import datetime
import os
import wolframalpha
import wikipedia
import requests
import webbrowser
import pause
import time
import psutil
import instaloader
import speech_recognition as sr
import pywhatkit as kit
from plyer import notification
from googletrans import Translator
from pygame import mixer
import pyttsx3

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
        audio = r.listen(source,0,8)
    try:
        print(": Recognizing.....")
        query = r.recognize_google(audio,language='en-pk')
    except:
        return ""
    query = str(query).lower()
    return query


def GenPass():
    p1 = string.ascii_letters
    p2 = string.ascii_lowercase
    p3 = string.ascii_uppercase
    p4 = string.digits
    p5 = string.punctuation
    p6 = string.octdigits
    p7 = string.whitespace
    PassLst = []
    PassLst.extend(list(p1))
    PassLst.extend(list(p2))
    PassLst.extend(list(p3))
    PassLst.extend(list(p4))
    PassLst.extend(list(p5))
    PassLst.extend(list(p6))
    PassLst.extend(list(p7))
    Speak("Sir, please enter your password length...")
    PassLen = int(input("Enter your password length: "))
    Speak("Sir, please tell me the file name to save your password...")
    File_name = Listen()
    PassPath = rf"D:\Python\New Jarvis\DataBase\Passwords\{File_name}"
    StrongPass = random.sample(PassLst, PassLen)
    EmptyStr = ""
    for Pass in PassLst:
        JoinPass = EmptyStr.join(StrongPass)
    with open(PassPath+".txt", 'w') as f:
        p = f.write(f"Your password is:\n{JoinPass}")
    Speak(f"Sir, your password is saved in {File_name}")
    os.startfile(rf"D:\Python\New Jarvis\DataBase\Passwords\{File_name}.txt")


def PassCrack():
    Speak("Enter your password to crack...")
    psswod = input("Enter your password: ")
    Speak("I am trying to crack your password...")
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
        'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'w', 'x', 'y', 'z']
    init_guess = ""
    while (init_guess != psswod):
        init_guess = ""
        for letter in range(len(psswod)):
            guess_letter = letters[(random.randint(0, 24))]
            init_guess = str(guess_letter) + str(init_guess)
            print(init_guess)

    Speak(f"Your password is: {init_guess}")


def Reader(BookName):

    if 'jarvis review' in BookName:
        os.startfile(r'D:\Python\New Jarvis\DataBase\PDF Books\JARVIS-Review-6.pdf')
        book = open(r'D:\Python\New Jarvis\DataBase\PDF Books\JARVIS-Review-6.pdf','rb')
        pdfreader = PyPDF2.PdfFileReader(book)
        pages = pdfreader.getNumPages()
        Speak(f"Number Of Pages In This Books Are {pages}")
        Speak("From Which Page I Have To Start Reading ?")
        numPage = int(input("Enter The Page Number :"))
        page = pdfreader.getPage(numPage)
        text = page.extractText()
        Speak(text)


def Notepad():
    Speak("Tell me what should I write...")
    writeab = input("Enter the text:\n")
    TimeOfNote = datetime.datetime.now().strftime("%H:%M:%S")
    Rep = TimeOfNote.replace(":", "-")
    FileName = Rep+"-note.txt"
    FilePath = f"D:\\Python\\New Jarvis\\DataBase\\NotePad\\{FileName}"
    with open(FilePath, "w") as f:
        f.write(str(writeab))
    os.startfile(FilePath)


def SheduleDay():
    tasks = [] #Empty list 
    Speak("Do you want to clear old tasks (Plz speak YES or NO)")
    query = Listen()
    if "yes" in query:
        file = open(rf"D:\Python\New Jarvis\DataBase\Tasks\{Date2()}-{tellDay2()}-{Year2()}-Task.txt","w")
        file.write(f"")
        file.close()
        Speak("Tell me the number of task for the day...")
        no_tasks = int(input("Enter the no. of tasks :- "))
        for i in range(no_tasks+1):
            Speak(f"Tell me the task {i}...")
            tasks.append(input("Enter the task :- "))
            file = open(rf"D:\Python\New Jarvis\DataBase\Tasks\{Date2()}-{tellDay2()}-{Year2()}-Task.txt","a")
            file.write(f"{i}. {tasks[i]}\n")
            file.close()
    elif "no" in query:
        Speak("Tell me the number of task for the day...")
        no_tasks = int(input("Enter the no. of tasks :- "))
        for i in range(no_tasks+1):
            Speak(f"Tell me the task {i}...")
            tasks.append(input("Enter the task :- "))
            file = open(rf"D:\Python\New Jarvis\DataBase\Tasks\{Date2()}-{tellDay2()}-{Year2()}-Task.txt","a")
            file.write(f"{i}. {tasks[i]}\n")
            file.close()


def CloseNotepad():
    os.system("TASKKILL /F /im Notepad.exe")


def NewFolder(Newfolder):
    Speak('tell me the path of the folder')
    path= input("Enter path> ")
    os.chdir(path)
    os.makedirs(Newfolder)
    Speak('i have  made a folder named ' +Newfolder+' in the given directry')
    os.system('"C:\\Users\\ADMIN\\Desktop\\VIRTUAL ASSISTANT\\ASSISTANT.py"')


def NoteTake():
    Speak("Sir tell me what is the note...")
    note = Listen()
    Speak("Now tell me the file name...")
    FileName = input("Enter file name: ")
    pathofnote = "D:\\Python\\New Jarvis\\DataBase\\Notes\\"
    with open(pathofnote+FileName+".txt", 'w') as f:
        f.write(str(f"Day: {tellDay2()}\n"))
        f.write(str(f"Date: {Date2()}\n"))
        f.write(str(f"Year: {Year2()}\n"))
        f.write(str(f"Time: {Time2()}\n\n"))
        f.write(str("Your Note:\n"))
        f.write(str(note))
        Speak("Note have been taken...")
        os.startfile(f"D:\\Python\\New Jarvis\\DataBase\\Notes\\{FileName}.txt")


def TimeTable():
    Speak("Checking your time table....")
    from DataBase.TimeTable.TimeTable import Time
    from Sounds import NotifySound
    value = Time()
    NotifySound()
    notification.notify(
        title = "Time Table",
        message = value ,           
        timeout= 15
    )
        # waiting time
    time.sleep(7)


def ShowShedule(date):
    file = open(rf"D:\Python\New Jarvis\DataBase\Tasks\{date}-Task.txt","r")
    content = file.read()
    file.close()
    mixer.init()
    mixer.music.load(r"D:\Python\New Jarvis\DataBase\Sounds\notification.mp3")
    mixer.music.play()
    notification.notify(
    title = "My Schedule :-",
    message = content,
    timeout = 15
    )


def TransUrdu():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='ur')
        print(f"User said: {query}\n")

    except:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def Trans():
    Speak("Tell me the line sir...")
    line = TransUrdu()
    Translate = Translator()
    result = Translate.translate(line)
    Text = result.text
    Speak("Translation for your line is...")
    Speak(Text)


def downInstaPro():
    Speak("sir, please enter the username correctly.")
    name = input("Enter the username here:")
    webbrowser.open(f"www.instagram.com/{name}")
    Speak(f"Sir,here is the profile of the user {name}")
    time.sleep(5)
    Speak("sir, would you like to download profile pic of this account.")
    condition = input("y(YES)/n(NO)> ")
    low_cond = condition.lower()
    if "y" in low_cond:
        mod = instaloader.Instaloader()
        mod.download_profile(name, profile_pic_only=True)
        Speak("i am done sir, profile pic is saved in main folder , now i am ready for next task")
    else:
        pass


def calculate(audio_data):
    client = wolframalpha.Client("8REQUG-YQ7JGY96T8")
    res = client.query(audio_data)
    try:
        Speak("Calculating...")
        time.sleep(5)
        Speak(next(res.results).text)
    except StopIteration:
        Speak("I have some problem but I am trying to evaluate it...")
        time.sleep(10)
        Query = str(audio_data)
        kit.search(Query)
        search = wikipedia.summary(Query, 2)
        Speak(f": According To Your Search : {search}")


def GK(qestion):
    client = wolframalpha.Client("8XQ97A-7EG5PX569E")
    res = client.query(qestion)
    try:
        Speak("Ok sir fetching the information...")
        Speak(next(res.results).text)
    except StopIteration:
        Speak("Sir I am searching in google...")
        Query = str(qestion)
        kit.search(Query)
        search = wikipedia.summary(Query, 2)
        Speak(f": According To Your Search : {search}")


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    Speak(res["joke"])


def tellJoke():
    Url = "https://v2.jokeapi.dev/joke/Any?safe-mode"
    r = requests.get(Url)
    Data = r.json()
    category = Data["category"]
    Type = Data["type"]
    joke = Data["setup"]
    delivery = Data["delivery"]
    Speak(f"Joke category is {category}")
    Speak(f"Joke type is {Type}")
    Speak(joke)
    Speak(delivery)


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def Time():
    strTime = datetime.datetime.now().strftime("%H")
    strTime2 = datetime.datetime.now().strftime("%M")
    strTime = int(strTime)
    strTime2 = int(strTime2)
    Speak(f"Sir, the time is {strTime}:{strTime2}")


def Date2():
    Date = datetime.datetime.now()
    Date = Date.strftime("%d")
    return Date


def Year2():
    year = datetime.datetime.now()
    year = year.strftime("%Y")
    return year


def tellDay2():
    NoteDay = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
    if NoteDay in Day_dict.keys():
        day_of_the_week = Day_dict[NoteDay]
        return day_of_the_week


def Time2():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    return strTime


def Acro():
    Speak("Sir please tell me a phrase...")
    phrase = Listen()
    phrase_split = phrase.split()
    acronym = ""
    for i in phrase_split:
        acronym = acronym + i[0].upper()
    Speak(f"The acronym for your phrase is {acronym}.")


def battery():
    battery = psutil.sensors_battery()
    battery_percentage = str(battery.percent)
    plugged = battery.power_plugged
    Speak(f"Sir, it is {battery_percentage} percent.")
    if plugged:
        Speak("and It is charging....")
    if not plugged:
        if battery_percentage <= "95%":
            Speak("Sir, plug charger.")


def weather_city(city_name):
    api_key = "a31701327639a3e2751b57480ed4b785"
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(
        city_name,api_key)
    res = requests.get(url)
    data = res.json()
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    description = data['weather'][0]['description']

    Speak(f'Temperature in {city_name} is {temp} degree celcius')
    Speak(f'On longitude of {longitude}')
    Speak(f'On latitude of {latitude}')
    Speak(f'Wind Speed is {wind_speed} meter per second')
    Speak(f'Description : {description}')


def weather_news(city_name):
    api_key = "69bf0a590576448ed0bfd804ac2b2694"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
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
        celsius = current_temperature-273.15
        Speak("Sir, Temperature in " + city_name +
              "is" + str(celsius) + " degree celsius")
        Speak("Temperature in Celsius is" + str(celsius) + " degree celsius")
        Speak("Temperature in Farenheit is " +
              str(celsius*9/5+32) + " degree farenheit")
        Speak("The weather description is " + weather_description)
        Speak("Atmospheric pressure is" + str(current_pressure))
        # Speak("Humidity is" , str(current_humidiy) , " %")
        print("")


def RandFact():
    url = "https://catfact.ninja/fact"
    r = requests.get(url)
    Data = r.json()
    title = Data["fact"]
    Speak(title)


def RandActivity():
    Url = "https://www.boredapi.com/api/activity"
    r = requests.get(Url)
    Data = r.json()
    Activity = Data["activity"]
    Type = Data["type"]
    Speak(f"Activity type {Type}")
    Speak(Activity)


def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date = Date.replace(" and ","-")
    Date = Date.replace("and","-")
    Date = Date.replace("and","-")
    Date = Date.replace(" ","")

    return str(Date)


def Alarm(query):

    TimeHere=  open('D:\\Python\\New Jarvis\\Data.txt','a')
    TimeHere.write(query)
    TimeHere.close()
    os.startfile("D:\\Python\\New Jarvis\\DataBase\\ExtraPro\\Alarm.py")


def DownloadYouTube():
    
    from pytube import YouTube
    from pyautogui import click
    from pyautogui import hotkey
    import pyperclip
    from time import sleep

    sleep(2)
    click(x=740, y=49)
    hotkey('ctrl','c')
    value = pyperclip.paste()
    Link = str(value) # Important 

    def Download(link):
        url = YouTube(link)
        video = url.streams.first()
        video.download('D:\\Python\\New Jarvis\\DataBase\\Youtube\\')
    Download(Link)
    Speak("Done Sir , I Have Downloaded The Video .")
    Speak("You Can Go And Check It Out.")
    os.startfile('D:\\Python\\New Jarvis\\DataBase\\Youtube\\')


def DogImg():
    Speak("Ok sir downloading dog images")
    Url = "https://dog.ceo/api/breeds/image/random"
    r = requests.get(Url)
    Data = r.json()
    # print(Data)
    DogPhoto = Data["message"]
    webbrowser.open(DogPhoto)
    Speak("I wish you liked this photo")


def Currency():
    Speak("Enter the country id...")
    Country = int(input("Enter country id: "))
    Url = "https://api.coinbase.com/v2/currencies"
    r = requests.get(Url)
    Data = r.json()
    Data2 = Data["data"][Country]
    Name = Data2["name"]
    min_size = Data2["min_size"]
    Speak(f"Sir the country you selected is {Name}")
    Speak(f"and sir the rate of the {Name} currency is {min_size}")


def HackRandom():
    Url = "https://randomuser.me/api/"
    r = requests.get(Url)
    Data = r.json()
    Result = Data["results"][0]
    Gender = Result["gender"]
    Name = Result["name"]
    First = Name["first"]
    Last = Name["last"]
    Location = Data["results"][0]["location"]
    Street = Location["street"]
    StreetNo = Street["number"]
    StreetName = Street["name"]
    City = Location["city"]
    state = Location["state"]
    Country = Location["country"]
    PostCode = Location["postcode"]
    Coord = Location["coordinates"]
    latitude = Coord["latitude"]
    longitude = Coord["longitude"]
    Email = Data["results"][0]
    Email_id = Email["email"]
    Login_info = Email["login"]
    username = Login_info["username"]
    password = Login_info["password"]
    Personal_info = Data["results"][0]
    Date = Personal_info["dob"]
    age = Date["age"]
    reg = Data["results"][0]["registered"]
    reg_age = reg["age"]
    phone_num = Data["results"][0]
    phone = phone_num["phone"]
    cell_phone = phone_num["cell"]
    img = Data["results"][0]
    person_img = img["picture"]
    large_img = person_img["large"]

    Speak("Sir hacking a random person online")
    Speak("Finding the target sir")
    pause.seconds(12)
    Speak("Sir target found")
    Speak("Now gaining as much information about the target from third party applications and websites")
    pause.seconds(12)
    Speak("Footprinting done")
    Speak("Now gaining access to his system")
    pause.seconds(8)
    Speak("Access has been granted")
    Speak(f"Sir the name of the hacked target is {First} {Last}")
    Speak(
        f"Sir your target lives in {Country}, state {state} and sir city {City}")
    Speak(f"Sir the street name of the target where he lives is {StreetName}")
    Speak(f"and sir the street number is {StreetNo}")
    Speak(f"Sir the age of the victom is {age}")
    Speak(f"Target gender is {Gender}")
    Speak(f"Phone number of the target is {phone}")
    Speak(f"and sir cell number of the target is {cell_phone}")
    Speak(
        f"Right now the position of the target is {latitude} latitude and {longitude} longitude")
    Speak(
       f"The email id of the target is {Email_id}, username is {username} and its password is {password}")
    webbrowser.open(large_img)
    Speak("and sir this the photo of the target")
    Speak("Cleaning all logs from the victom system, or you will be arrested by police officers.")
    pause.seconds(14)
    Speak("Logs has been cleared")


def My_details():
    Url = "https://freegeoip.app/json/"
    r = requests.get(Url)
    Data = r.json()
    print(Data)
    ip = Data["ip"]
    country_code = Data["country_code"]
    country_name = Data["country_name"]
    region_code = Data["region_code"]
    region_name = Data["region_name"]
    city = Data["city"]
    zip_code = Data["zip_code"]
    time_zone = Data["time_zone"]
    latitude = Data["latitude"]
    longitude = Data["longitude"]
    Speak(f"Sir your ip address is {ip}")
    Speak(f"Sir you live in {country_name}")
    Speak(f"Sir the country code of {country_name} is {country_code}")
    Speak(f"Region code of {region_name} is {region_code}")
    Speak(f"Sir the city in which in you live is {city}")
    Speak(f"Sir the zip code of {city} is {zip_code}")
    Speak(f"Sir the time zone of {country_name} is {time_zone}")
    Speak(f"Sir right now your position in latitude is {latitude}")
    Speak(f"and sir position in longitude is {longitude}")

