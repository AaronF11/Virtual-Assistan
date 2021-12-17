# --------------- headers --------------- #
from os import system
from utils import *
import datetime
import pywhatkit


# --------------- Functions engine_of_voice --------------- #
# Voices
    # Spanish-Mexican[0]
    # English-EUA[1]

def engine_of_voice_sp(text):
    
    engine.setProperty('voice', voices[0].id)       
    engine.say(text)
    engine.runAndWait()

def engine_of_voice_en(text):
    engine.setProperty('voice', voices[1].id)       
    engine.say(text)
    engine.runAndWait()


# --------------- Function listening --------------- #
def listen():
    try:
        with SR.Microphone() as source:
            system('cls')
            print(""" - - - SELECT A LENGUAGE - - - 
            + SPANISH
            + ENGLISH""")
            voice = listener.listen(source)
            recognizer = listener.recognize_google(voice)
            recognizer = recognizer.lower()

            if 'spanish' in recognizer:
                try:
                    with SR.Microphone() as source:
                        print(listening[0])
                        voice = listener.listen(source)
                        recognizer = listener.recognize_google(voice)
                        recognizer = recognizer.lower()    
                except:
                    print(repeat[0])
                    engine_of_voice_sp(repeat[0])
                    listen()

                return recognizer

            if 'english' in recognizer:
                try:
                    with SR.Microphone() as source:
                        print(listening[1])
                        voice = listener.listen(source)
                        recognizer = listener.recognize_google(voice)
                        recognizer = recognizer.lower()    
                except:
                    print(repeat[1])
                    engine_of_voice_en(repeat[1])
                    listen()

                return recognizer
    except:
        print(repeat[1])
        engine_of_voice_en(repeat[1])
        listen()
        
    
# --------------- Function action --------------- #
def action():
    recognizer = listen()

    # --------------- Play on Youtube --------------- #
    if 'reproduce' in recognizer:
        new = recognizer.replace('alexa reproduce', '')
        engine_of_voice_sp(list_actions[0]+new)
        pywhatkit.playonyt(new)
        print(playing[0])
    
    elif 'play' in recognizer:
        new = recognizer.replace('alexa play', '')
        engine_of_voice_en(list_actions[1]+new)
        pywhatkit.playonyt(new)
        print(playing[1])
        
    # --------------- Search on Google --------------- #
    

    # --------------- Time --------------- #
    if 'tiempo' in recognizer:
        new = datetime.datetime.now().strftime('%H:%M %p')
        print("SON LAS" + new)
        engine_of_voice_sp("SON LAS" + new)
    
    elif 'time' in recognizer:
        new = datetime.datetime.now().strftime('%H:%M %p')
        print("IT'S" + new)
        engine_of_voice_en("IT'S" + new)

    # --------------- Date --------------- #
    if 'calendario' in recognizer:
        new = datetime.datetime.now().strftime('%Y:%M:%D')
        print("ESTAMOS A" + new)
        engine_of_voice_sp("ESTAMOS A" + new)
    
    elif 'date' in recognizer:
        new = datetime.datetime.now().strftime('%Y:%M:%D')
        print("ESTAMOS A" + new)
        engine_of_voice_en("ESTAMOS A" + new)
    


# --------------- main --------------- #
def main():
    action()
    