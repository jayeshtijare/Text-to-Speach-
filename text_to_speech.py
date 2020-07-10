from gtts import gTTS
import os

f=open('text.txt','r')
text1= f.read()

language= 'en'

audio= gTTS(text=text1,lang=language,slow=False)

audio.save("text to audio.wav")
os.system("text to audio.wav")