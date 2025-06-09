#!/usr/bin/python3

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import os
import wikipedia
import webbrowser
import pyjokes
import pyautogui 

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

'''
for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name}, ID: {voice.id}, Lang: {voice.languages}")
'''

engine.setProperty('voice', voices[24].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()
    
def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print("Listening ..")
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            if 'Alexa' in command:
                command = command.replace('Alexa','')
    except:
        pass
    return(command)

def run_alexa():
    command = take_command()
    
    if not command:
        return 
    
    if 'play' in command:
        song = command.replace('play', '')
        talk(f'playing {song}')
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M/%p')
        talk(f'time is {time}')
    
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%d%B%Y')
        talk(f"Today's date is {date}")
    
    elif 'search for' in command:
        query = command.replace('search for', '').strip()
        if query:
            try:
                info = wikipedia.summary(query, sentences=1)
                print(info)
                talk(info)
            except wikipedia.exceptions.DisambiguationError as e:
                talk("Your search was too broad. Please be more specific.")
            except wikipedia.exceptions.PageError:
                talk("I couldn't find any result. Try again.")
            except Exception as e:
                talk("An error occurred while searching.")
        else:
            talk("I didn't hear what to search for. Please say the command again.")
    
    elif 'google' in command:
        talk('Opening google')
        webbrowser.open('https://www.google.com/')
        
    elif 'youtube' in command:
        talk('Opening youtube')
        webbrowser.open('https://www.youtube.com/')
    
    elif 'code' in command:
        talk('Opening vs code')
        os.system('code')
    
    elif 'terminal' in command:
        talk('Opening Terminal')
        os.system('konsole')
        
    elif 'screenshot' in command:
        talk('Taking screenshot')
        pyautogui.screenshot()
    
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        
    else:
        talk("Can't understand, Say the command again! ")

talk('Hello Basmala, What can I do for you?')

while True:
    run_alexa()