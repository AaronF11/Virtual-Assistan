# --------------- headers --------------- #
import pyttsx3


# --------------- varibles of engine_of_voice --------------- #
engine = pyttsx3.init()
voices = engine.getProperty('voices')
# Voices
    # Spanish-Mexican[0]
    # Spanish-Spain[1]
    # English-EUA[2]
engine.setProperty('voice', voices[0].id)


# --------------- varibles of listening--------------- #