from gtts import gTTS

text = "This is Project 03"  # Bind a string to the text variable.

language = 'en'             # Language in which you want to convert

tts = gTTS(text=text, lang=language)       # Convert the string and bind it to the tts variable.
# Convert text to voice and save the file name as hello.mp3.
tts.save(r"3. Convert text to speech\hello.mp3")