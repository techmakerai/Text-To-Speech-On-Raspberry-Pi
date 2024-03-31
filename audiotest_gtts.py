# Text-To-Speech Translation with Python and Google TTS
# By TechMakerAI on YouTube 
# 
from gtts import gTTS
import os
from io import BytesIO
from pygame import mixer

mixer.init()

mp3audio = BytesIO()

text = 'Hi,there,how can I help you? This is the second sentence of the paragraph. This is the third sentence of the paragraph.'
  

tts = gTTS(text, lang='en', tld = 'us')
 
        
tts.write_to_fp(mp3audio)

mp3audio.seek(0)

mixer.music.load(mp3audio, "mp3")
mixer.music.play()

while mixer.music.get_busy():
    pass
    

