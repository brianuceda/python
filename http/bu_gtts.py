from gtts import gTTS
import os

# Texto en español
text = "Hola."

# Configurar TTS en español
tts = gTTS(text=text, lang='es')

# Guardar el archivo de audio
tts.save("output.mp3")

# Reproducir el archivo de audio
os.system("mpg321 output.mp3")
