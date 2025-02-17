from gtts import gTTS
from playsound import playsound
import os

#Moving file paths
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = 'Project3Text.txt'
with open(file_path, 'rt', encoding= 'UTF8') as f :
    read_file = f.read()

tts = gTTS(text=read_file, lang='ko')

tts.save("myText.mp3")

playsound("myText.mp3")