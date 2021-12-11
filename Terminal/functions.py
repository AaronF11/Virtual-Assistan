# --------------- headers --------------- #
from utils import *


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
                        if 'alexa' in recognizer:
                            engine_of_voice_sp(recognizer)    
                except:
                    print(repeat[0])

                return recognizer

            if 'english' in recognizer:
                try:
                    with SR.Microphone() as source:
                        print(listening[1])
                        voice = listener.listen(source)
                        recognizer = listener.recognize_google(voice)
                        recognizer = recognizer.lower()
                        if 'alexa' in recognizer:
                            engine_of_voice_en(recognizer)    
                except:
                    print(repeat[1])

                return recognizer
    except:
        pass
        
    
# --------------- Function action --------------- #
def action():
    recognizer = listen()

    if 'reproduce' in recognizer:
        print(playing[0])
    
    if 'play' in recognizer:
        print(playing[1])


# --------------- main --------------- #
def main():
    action()
    