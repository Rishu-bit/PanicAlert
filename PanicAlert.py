import speech_recognition as sr
import pyttsx3
import requests
import json
import smtplib
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def sendmailfunction(recieveraddress,latitude,longitude,currentcity):
    msg=EmailMessage();
    msg['Subject']='PANIC ALERT'
    msg['From']='FROM SENDER'
    msg['To']=recieveraddress
    msg.set_content("someone is in danger!"+ "https://maps.google.com/?q="+latitude+","+longitude)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login("panicalertnotice@gmail.com","Asdfghjkl12345@")
    server.send_message(msg)
    server.quit();
    print("Mail sent to : ",currentcity)

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if(command == "help"):
                res = requests.get('https://ipinfo.io/')
                data = res.json()
                print(data)
                location = data['loc'].split(',')
                latitude = location[0]
                longitude = location[1]
                print("Latitude : ", latitude)
                print("Longitude : ", longitude)
                currentcity = data['city']
                if(currentcity == "Bhubaneshwar" or currentcity == "Āthagarh"):
                    # send mail to bhubaneshwar
                    recieveradress="tiwari2366@gmail.com"
                    sendmailfunction(recieveradress,latitude,longitude,currentcity)
                elif (currentcity == "Hyderabad"):
                    # send mail to hyderabad
                    recieveradress="sauravkumarsahoo123@gmail.com"
                    sendmailfunction(recieveradress,latitude,longitude,currentcity)
                elif (currentcity == "Ranchi"):
                    recieveradress="ananyaraj1709@gmail.com"
                    sendmailfunction(recieveradress,latitude,longitude,currentcity)
                    
    except:
        pass
    return command


while True:
    check = take_command()
    if(check=="help"):
        break
    if(check != "help" or check!="bachao"):
        print("invalid command")
