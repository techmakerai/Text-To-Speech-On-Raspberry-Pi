# Text-To-Speech Translation with Piper TTS and Python 
# TechMakerAI on YouTube

from piper import PiperVoice
import wave  
from io import BytesIO
from pygame import mixer

mixer.init()

wavaudio = BytesIO()

voice = PiperVoice.load('/home/pi/piper/voice/ryan/en_US-ryan-medium.onnx', 
	config_path='/home/pi/piper/voice/ryan/en_US-ryan-medium.onnx.json')

text = 'Hi,there,how can I help you? This is the second sentence of the paragraph. This is the third sentence of the paragraph. '
  
with wave.open(wavaudio, "wb") as wav_file:
    voice.synthesize(text, wav_file)
    wav_file.close()

wavaudio.seek(0)

mixer.music.load(wavaudio, "wav")
mixer.music.play()

while mixer.music.get_busy():
    pass


