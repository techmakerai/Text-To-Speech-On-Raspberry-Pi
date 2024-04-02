# Text-To-Speech Translation with Piper TTS (Stream) and Python 
# TechMakerAI on YouTube

import numpy as np
from piper import PiperVoice
import sounddevice as sd

voice = PiperVoice.load('/home/pi/piper/voice/ryan/en_US-ryan-medium.onnx', 
	config_path='/home/pi/piper/voice/ryan/en_US-ryan-medium.onnx.json')

text = 'Hi,there,how can I help you? This is the second sentence of the paragraph. This is the third sentence of the paragraph. '

# Create a sounddevice stream  
stream = sd.OutputStream(samplerate=22050, channels=1, dtype='int16')
stream.start()

for audio_bytes in voice.synthesize_stream_raw(text):
    int_data = np.frombuffer(audio_bytes, dtype=np.int16)
    stream.write(int_data)

stream.stop()
stream.close()

