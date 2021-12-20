# --------------- headers --------------- #
from os import system
from utils import *
import datetime
import pywhatkit
import wikipedia

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

                return recognizer

            else:
                engine_of_voice_en(invalid[1])
                print(repeat[1])
                engine_of_voice_en(repeat[1])
                listen()    
    except:
        listen()

    
# --------------- Function action --------------- #
def action():
    recognizer = listen()
    while True:
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
        elif 'busca' in recognizer:
            new = recognizer.replace('alexa busca', '')
            engine_of_voice_sp(list_actions[2]+new)
            pywhatkit.search(new)
            print(searching[0])
        elif 'search' in recognizer:
            new = recognizer.replace('alexa search', '')
            engine_of_voice_en(list_actions[3]+new)
            pywhatkit.search(new)
            print(searching[1])
            
        # --------------- Search on Wikipedia --------------- #
        elif 'wikipedia' in recognizer:
            new = recognizer.replace('alexa wikipedia', '')
            engine_of_voice_sp(new)
            info = wikipedia.summary(new, 1)
            print(wiki[0])
            engine_of_voice_sp(info)
        elif 'what is' in recognizer:
            new = recognizer.replace('alexa what is', '')
            engine_of_voice_en(new)
            info = wikipedia.summary(new, 1)
            print(wiki[1])
            engine_of_voice_en(info)

        # --------------- Time --------------- #
        elif 'tiempo' in recognizer:
            new = datetime.datetime.now().strftime('%H:%M %p')
            print("SON LAS" + new)
            engine_of_voice_sp("SON LAS" + new)
        
        elif 'time' in recognizer:
            new = datetime.datetime.now().strftime('%H:%M %p')
            print("IT'S" + new)
            engine_of_voice_en("IT'S" + new)

        # --------------- Date --------------- #
        elif 'calendario' in recognizer:
            new = datetime.datetime.now().strftime('%Y:%M:%D')
            print("ESTAMOS A" + new)
            engine_of_voice_sp("ESTAMOS A" + new)
        
        elif 'date' in recognizer:
            new = datetime.datetime.now().strftime('%Y:%M:%D')
            print("ESTAMOS A" + new)
            engine_of_voice_en("ESTAMOS A" + new)

        else:
            engine_of_voice_en(invalid[1])
            print(repeat[1])
            engine_of_voice_en(repeat[1])
            action() 


# --------------- main --------------- #
def main():
    action()