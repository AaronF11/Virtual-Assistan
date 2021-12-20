# --------------- headers --------------- #
import pyttsx3
import speech_recognition as SR


# --------------- varibles of engine_of_voice --------------- #
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# --------------- varibles of listening--------------- #
listener = SR.Recognizer()
listening = ["ESCUCHANDO...",
             "LISTENING..."]

repeat = ["REPITE PORFAVOR...",
          "REPEAT PLEASE..."]

playing = ["REPRODUCIENDO...",
           "PLAYING..."]

searching = ["BUSCANDO...",
             "SEARCHING..."]

wiki = ["HABLANDO...",
        "TALKING..."]

IA = "alexa"

# --------------- varibles of action--------------- #
invalid = ["COMANDO INVALIDO...",
          "INVALID COMMAND..."]

list_actions = ["reproduciendo",
                "playing",
                "buscando",
                "searching"]

