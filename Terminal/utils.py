# --------------- headers --------------- #
import pyttsx3
import speech_recognition as SR


# --------------- varibles of engine_of_voice --------------- #
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# --------------- varibles of listening--------------- #
listener = SR.Recognizer()

listening = ["ESCUCHANDO...", "LISTENING..."]
repeat = ["REPITE PORFAVOR...","REPEAT PLEASE..."]
playing = ["REPRODUCIENDO...", "PLAYING..."]
IA = "alexa"