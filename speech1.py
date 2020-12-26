
import speech_recognition as sr
from gtts import gTTS
import os
import pygame
import sys
import webbrowser
import wikipedia
import smtplib
import pyglet
from datetime import datetime
import pandas as pd
def TimeH():
    n=datetime.now()
    currenthour=n.strftime("%H")
    return currenthour
def TimeM():
    n=datetime.now()
    currentminute=n.strftime("%M")
    return currentminute
def Time():
    n=datetime.now()
    currenttime=n.strftime("%H%M")
    return currenttime
get=False
listened=False
#emails
Kanchan="kanchan.singh1098@gmail.com"
Praveen="praveen.ithacker@gmail.com"
Me="nitesh.singh5695@gmail.com"
def wait(second):
 pygame.time.wait(second)
def yes():
     text=="are you sure..  sir.."
     bol()
     text=listen()

def hear():
    s=r.listen(source)
    find=r.recognize_google(s)
    search=('https://www.google.com/search?q='+find)
    webbrowser.open_new(search)

def listen():
 while not listened:
    print('listening..')
    s=r.listen(source)
    print('listened')
    return r.recognize_google(s)
    listened=False

def web():
    webbrowser.open_new('https://www.youtube.com/watch?v=TBAj4nbdLEU')
def song():
    get=False
    while not get:
         s=r.listen(source)
         try:
             song=r.recognize_google(s)
             print(song)
             music=(song+".mp3")
             os.chdir('E:\Enterntment\Songs\Audio')
             os.startfile(music)
             get=True


         except:
          print("not listen")

def display():
    pygame.init()
    screen=pygame.display.set_mode((280,200))
    bg=pygame.image.load("jarvis.jpg")
    bg=pygame.transform.scale(bg,(280,200))
    screen.blit(bg,(0,0))
    pygame.display.update()

display()
def event():
 for event in pygame.event.get():
                 if event.type== pygame.QUIT:
                    sys.exit()
def bol():
 speak=gTTS(text,lang="en",slow=False)
 speak.save("speech.mp3")
 music=pyglet.media.load("speech.mp3")
 music.play()
 #os.remove("speech.mp3")
over=False
#display()
def bolslow():
    speak=gTTS(text,lang="en",slow=True)
    speak.save("speech1.mp3")
    Music=pyglet.media.load("speech1.mp3")
    Music.play()
r = sr.Recognizer()
with sr.Microphone() as source:
    text="hello sir"
    bol()
    wait(1000)
    while not over:
     event()
     print("tell me i'm listening..")
     r.pause_threshold =1
     r.adjust_for_ambient_noise(source,duration =1)
     audio = r.listen(source)

     print("processing.......")
     try:
        text = r.recognize_google(audio)
        text=text.lower()
        print(text)
       #text =input("say something")
        print("you said :"+text)
     except:
        print("sorry could not recognize your voice")
        text="error"

       #text =input("say something")
        print("you said :"+text)
     if text=="how are you":
         text="i am fine sir"
         bol()
     elif  text=="open chrome" or text=="open browser" :
         text="chrome is opening"
         bol()
         os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
     elif text=="open youtube":
         text="opening youtube"
         bol()
         webbrowser.open_new("www.youtube.com")
     elif text=="stop chrome" or text=="close chrome" or text=="exit chrome" :
         os.system('TASKKILL /F /IM chrome.exe')
     elif text=="open music" or text=="play music" or text=="play songs" or "song" in text:                          #MUSIC
         text="which song   sir.."

         bol()
         song()

     elif text=="who are you" or text=="what is your identity" or "your" in text:
         text="i am tanya and i am simple programme coded in python and... i am totally differents from human"
         bol()

     elif "satya" in text:
          text="satya is your good friend and he is also your classmate"
          bol()
     elif text=="hi" or   text=="hello" or  text=="hey":
           text="hello sir"
           bolslow()
     elif text=="stop music":
          text="ok sir"
          stop="TASKKILL /F /IM GrooveMusic.exe"                                                          #fix it
          os.system(stop)
     elif text=="close all program" or text=="close all task" or text=="stop all program" or text=="exit all programs" or text=="exit programs":
         text="are you sure to close all program"
         bol()
         text=listen()
         if text=="yes" or text=="haan":                                                                             #not working
              text="ok sir...closing all programs"
              os.system("TASKKILL /F /IM *exe")
     elif text == "search" :
          text = "on which thing ..... sir"
          bol()
          hear()
     elif text=="open pub ji" or "pub" in text :
         text="got it"
         bol()
         try:
          os.startfile('D:\Program Files\TxGameAssistant\AppMarket\AppMarket.exe')
         except:
             text="unable to open"
             bol()
     elif text == "bye bye" or text=="get lost" or text=="exit" or "bye" in text or "bhaag" in text or "bhag" in text:
          text="good bye...    sir.. "
          bolslow()
          pygame.time.wait(1000)
          sys.exit()

     elif text=="sleep" or text=="turn pc in sleep mode" or text=="activate sleep mode" or text=="get in sleep mode" or text=="turn on sleep mode":

           text="are you sure..  sir.."
           bol()
           text=listen()


           if text=="yes" or text=="haan":
             text="ok..    sir..   your pc is going in sleep mode"
             bol()
             wait(10000)

             os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
     elif "shutdown" in text or "turn off" in text:
           text="are you sure to shutdown computer"
           bol()
           text=listen()
           if text=="yes" or text=="haan":
                text="your system will be shutdown in ten seconds"
                bol()
                wait(2000)
                text="good bye...     sir.."
                bol()

                os.system("SHUTDOWN/F/T 1")
     elif text=="are you listening" or text=="tanya" or text=="are you  hear me" or "sun rahi" in text   or text=="sun rahi hai":
         text="yes sir "
         bolslow()
         text="i am listening"
         bol()
         text="yes sir"
         bol()
     elif text=="send mail" or text=="send message" or text=="send a mail" or "message" in text :
         try :
              text="ok   sir.."
              bol()
              text=" but... who is recipient"
              bol()
              reciever=listen()
              if "Kanchan" in reciever:
                  reciever="kanchan.singh1098@gmail.com"
              elif "Satya" in reciever:
                  reciever="satyabrata12017@gmail.com"
              elif "Nitesh" in reciever:
                  text="sir...   you want.. to send message yourself"
                  bol()
                  text=listen()

                  if "yes" in text:
                      reciever="nitesh.singh5695@gmail.com"
              else:
                  text="this person is not in your contact list"
                  bol()

              #reciever=
              obj=smtplib.SMTP('smtp.gmail.com',587)
              text="processing please wait"
              bol()
              obj.ehlo()
              obj.starttls()
              obj.login("tanya.assistant1916@gmail.com","TANYA 1916")
              text="try to log in my account..."
              bol()
              text="log in successful"
              bol()
              text="what i message him"
              bol()
              message="hello sir/mam i am TANYA .. Assistant of NITESH SINGH. \n " \
                      "this Mail was send by me...  Sir wants to say you something \n" \
                      "here is meassage...\n" \
                      "...........\n"+ listen()+".\n"\
                      "...............message ..end.......\n"
              print(message)

              obj.sendmail('tanya.assistant1916@gmail.com',reciever,message)
              obj.close()
              text="sent mail succesfully"
              bol()
         except :
             text="could not sent mail something.. wrong.."
             bol()

     elif "question" in text or "when" in text or "what" in text or "wikipedia" in text:


         try:
          read =wikipedia.summary(text,sentences=2)
          text="according to me"
          bol()
          text=read
          bol()


         except:
          text="sir... i don't know....and your question may be wrong"
          bol()
          #os.remove("speech.mp3")
     elif "timer" in text:
         M=TimeM()
         text="for how much time"
         bol()
         try:


            print(c)
         except:
            text="please tell only integer value.. at... one time"
            bol()


     elif TimeM()== int(TimeM())+1:
         text="time finished"
         bol()
     elif text=="error":
         text="could not recognize"
         bol()
     elif "update command" in text or "add command" in text:
         text="ok sir"
         bol()
         text="please verify that it is you....       by giving your name and password"
         bol()
         text=listen()
         print(text)
         if "Nitesh" in text or "5695" in text:
            text="authorization successful"
            bol()
            text="tell the command"
            bol()

            data=pd.read_csv("command.csv", index_col=[0])
            answers=data.iloc[:,1].values
            commands=data.iloc[:,0].values
            no=data.iloc[:,2].values
            print(no)
            n=no[0]
            print(n)


            cmd=listen()
            data.set_value(n+1,"command",cmd)
            text="tell the answer"
            bol()
            ans=listen()
            data.set_value(n+1,"answer",ans)

            data.set_value(1,"cmd_no",n+1)
            data.to_csv("command.csv" )
            print(data)
         else:
             text="authorization failed"
             bol()
