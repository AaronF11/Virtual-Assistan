# --------------- headers --------------- #
from utils import *
import speech_recognition as SR

# --------------- Functions --------------- #
def engine_of_voice(text):
    engine.say(text)
    engine.runAndWait()

def listening():
    listener = SR.Recognizer()
    try:
        with SR.Microphone() as source:
            print("LISTENING...")
            voice = listener.listen(source)
            rec = listener.recognize_google(voice)
            print(rec)
            engine_of_voice(rec)
    except :
        print("REPEAT PLEAS")

# --------------- main --------------- #
def main():
    listening()
    