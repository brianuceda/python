from flask import Flask, request, send_file
from gtts import gTTS
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    text = 'TEAMO'
    print(f"Text received: {text}")  # Log para verificar el texto recibido

    tts = gTTS(text=text, lang='es')

    file_path = "output.mp3"
    if os.path.exists(file_path):
        os.remove(file_path)
    tts.save(file_path)
    
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
