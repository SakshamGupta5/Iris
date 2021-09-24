import os
from googlesearch import search
import pyttsx3
import pyaudio as pa
import datetime as dt
import pywhatkit as pw
import numpy as np
import News_headlines as nh
import datetime
import PyPDF2 as pp
import wikipedia as wk
import speech_recognition as sr
import jokes as pj
import Weather_fetcher as wf
from PIL import ImageTk,Image
import PIL.Image
from tkinter import Tk, Canvas
from tkinter import *
import smtplib
import webbrowser
import time

def setup():
    global nme
    
    speak("Heya. This is Iris, your personal desktop voice assistant. What shall I call you?")

    nme = rec_user()

    while True: 
        speak('Just to confirm, did you say' + nme + '?')
        confirm_nme = rec_user()
        if confirm_nme.lower() in 'yesyeahyupyesitisyesidid':
            break
        speak('Oh, ok. Please speak clearly into the microphone again. What shall I call you?')
        nme = rec_user()


    greet()

def wa():
    p_dir = {'dad':'+971502834557', 'mom':'+971547700053', 'mum':'+971547700053', 'mam':'+971547700053'}   
    speak('Ok' + nme + '! Who would you like to send a whatsapp message to?')
    recip = rec_user()

    speak('Cool! What would you like to send to ' + recip)
    content = rec_user()
    
    pw.sendwhatmsg(p_dir[recip.lower()], content, dt.datetime.now().hour, dt.datetime.now().minute + 2, wait_time = 45)
    
def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()

def rec_user():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        sysd.config(text = "Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        sysd.config(text = "Processing...")    
        query = r.recognize_google(audio, language='en-in')
        sysd.config(text = "System detects - " + query)

    except Exception as e:
        # print(e)    
        sysd.config(text = "Say that again please...")  
        return "None"
    
    return query


def greet():
    if dt.datetime.now().hour <= 12 and dt.datetime.now().hour >= 0:
        time = 'morning'
    elif dt.datetime.now().hour > 12 and dt.datetime.now().hour <=3:
        time = 'afternoon'
    else:
        time = 'evening'

    speak('Good ' + time + nme + '. Without any further delay, you may click on the speaker icon and begin speaking commands into your microphone. If you are a new user, please click on the help icon for some general guidelines to maximize the utility of this application.')

def moreinfo():
    #sysd.config(text = 'Hey '+ nme + '. Iris here. Thank you for choosing this service. Please listen carefully. Throughout the course of this application, you will be presented with a directory of functionalities you can vocally trigger. What is displayed above it is what the system detects from the user, followed by confirmation with a simple yes or no. A pause of greater than 1 seconds will be interpreted by me as the end of a command. If you wish to quit the application at any point of time, simply say QUIT.')
    speak('Hey '+ nme + '. Iris here. Thank you for choosing this service. Please listen carefully. Throughout the course of this application, you are entitled to a directory of functionalities you can vocally trigger. What is displayed below it is what the system detects from the user, followed by confirmation with a simple yes or no. However, the system detects feature may be buggy since python freezes the tkinter window while speech recognition takes place. A pause of greater than 1 second will be interpreted by me as the end of a command. If you wish to quit the application at any point of time, simply say QUIT.')

def core():
    user_response = rec_user()

    while 'quit' not in user_response:
        if 'time' in user_response:
            speak('It is currently ' + str(datetime.datetime.now().hour) + ' hours ' + str(datetime.datetime.now().minute) + ' minutes')
            return
        elif 'date' in user_response:
            months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'novemeber', 'december']
            speak(months[datetime.datetime.now().month + 1] + str(datetime.datetime.now().day) + ' ' + str(datetime.datetime.now().year))
            return
        elif 'joke' in user_response:
            speak('Hmm. I am still working on my currently awful sense of humor, but here it goes!' + pj.get_joke())
            return
        elif ('send an email' in user_response) or ('send email' in user_response) or ('send a mail' in user_response) or ('send mail' in user_response):
            directory = {'rimjhim':'singhrimjhim2017@gmail.com', 'dad':'singhrohit02011@gmail.com', 'mom':'singhreena02018@gmail.com', 'mum':'singhreena02018@gmail.com', 'mam':'singhreena02018@gmail.com', 'teacher':'safeera.hilal@ihs.edu'}
            speak('We are still working sending emails, ' + nme)
            return
        elif 'send a whatsapp message' in user_response or 'send whatsapp message' in user_response or 'send a message' in user_response or 'send message' in user_response or 'whatsapp' in user_response:
            wa()
            return
        elif 'open google' in user_response.lower():
            speak('opening google for you' + nme)
            webbrowser.open('https://www.google.com')
            return
        elif 'open facebook' in user_response.lower():
            speak('opening facebook for you' + nme)
            webbrowser.open('https://www.facebook.com')
            return
        elif 'open twitter' in user_response.lower():
            speak('opening twitter for you' + nme)
            webbrowser.open('https://www.twitter.com')
            return
        elif 'open youtube' in user_response.lower():
            speak('opening youtube for you' + nme)
            webbrowser.open('https://www.youtube.com')
            return
        elif 'play music' in user_response.lower():
            music_dir = 'D:\\test_music'
            songs = os.listdir(music_dir)    
            os.startfile(os.path.join(music_dir, songs[0]))
            return
        elif 'wikipedia' in user_response.lower():
            speak('what would you like to search on wikipedia ' + nme)
            sea = rec_user()
            speak('Give me a moment' + nme)
            results = wk.summary(sea,sentences=15)

            subroot = Tk()
            subroot.configure(bg = 'black')
            s1 = Label(subroot, text = results)
            s1.pack()
            s1.config(bg = 'white')
            subroot.geometry('800x600')
            subroot.mainloop()
            

            subroot.destroy()
            
            return
        elif 'google search' in user_response.lower():
            speak('what would you like to search on google ' + nme)
            sea = rec_user()
            speak('Give me a moment' + nme)
            result = ""
            for i in search(sea, tld="co.in", num=7, stop=7, pause=2):
                result += (i + '\n')

            subroot = Tk()
            subroot.configure(bg = 'black')
            s1 = Label(subroot, text = result)
            s1.pack()
            s1.config(bg = 'white')
            subroot.geometry('800x600')
            subroot.mainloop()
            speak('These are the top links on google for the search of' + sea)
            time.sleep(5)

            subroot.destroy()
            
            return
        elif 'read a pdf document' in user_response.lower() or 'read a pdf file' in user_response.lower():
            speak('Ok ' + nme + '! What is the name of the pdf file?')
            fi = rec_user()
            
            with open(fi + '.pdf','rb') as source:
                book = pp.PdfFileReader(source, strict = False)
                for i in range(book.numPages):
                    page = book.getPage(i)
                    text = page.extractText()
                    speak(text)
            return
        elif 'how i look' in user_response.lower() or 'how do i look' in user_response.lower():
            speak('Alright give me a moment')
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Snap Inc\Snap Camera.lnk')
            speak('Why dont you see for yourself, ' + nme)
            return
        elif 'weather' in user_response.lower():
            speak('Alright, tell me which locations weather do you want to know ' + nme)
            loc = rec_user()
            speak('Hmm. Just a moment.')
            speak(wf.get_w(loc))
            return
        elif 'news' in user_response.lower() or 'daily news' in user_response.lower() or 'news headlines' in user_response.lower():
            speak('The top 3 news headlines for today are as follows ' + nme)
            for i in range(2):
                speak(nh.get_news(i))
            return
        else:
            speak('sorry' + nme + 'that is not a registered command as of now')
            return
        
    speak('Alright then, until next time, ' + nme)

    root.destroy()

root= Tk()
root.title('  Personal Voice Assistant')
root.iconbitmap('spic.ico')
root.configure(bg = 'black')

my_img = PIL.Image.open('s4.png')
photo = ImageTk.PhotoImage(my_img)

my_label = Label(image = photo)
my_label.pack(pady = 30)

register = Button(command = setup, width = 15, height = 2, text = '⚙️ - S e t u p')
register.pack(pady = 30)

listen = Button(command = core, width = 15, height = 2, text = '🔊 - S p e a k')
listen.pack()

repeat = Button(command = moreinfo, width = 15, height = 2, text = '❗ - H e l p')
repeat.pack(pady = 30)

sysd = Label(borderwidth = 12, relief= 'raised', text = 'System detects - ', height = 6, width = 55)
sysd.pack(pady = 20)
sysd.config(bg = 'black')
sysd.config(fg = 'white')


repeat.config(command = moreinfo)
listen.config(command = core)

root.geometry('850x750')
root.mainloop()
