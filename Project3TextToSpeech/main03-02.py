from gtts import gTTS
from playsound import playsound 
import os 

os.chdir(os.path.dirname(os.path.abspath(__file__)))

text = "Hello World! This is Python Project 3!"

tts = gTTS(text=text, lang = 'en')
tts.save("hi.mp3")

playsound("hi.mp3")
