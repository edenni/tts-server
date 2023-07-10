import base64
import io
import json
import os
import requests
import wave

from flask import Flask, Response, request
from pydub import AudioSegment


PADDLE_PORT = os.environ.get("PADDLE_PORT", 8090)
paddle_url = f"http://localhost:{PADDLE_PORT}/paddlespeech/tts"

app = Flask(__name__)


@app.route("/tts", methods=["GET", "POST"])
def streamwav():
    data = json.loads(str(request.data, encoding="utf-8"))
    text = data["text"]

    # Post to the PaddleSpeech server
    data = {"text": text}
    response = requests.post(paddle_url, data=json.dumps(data))

    # Retrieve audio data, and some metadata
    result = response.json()["result"]
    audio_array = result['audio']
    audio_array = base64.b64decode(audio_array)
    sample_rate = result["sample_rate"]
    
    # Define the necessary parameters
    sample_width = 2  # Number of bytes per sample (16-bit audio)
    channels = 1  # Number of audio channels (1 for mono, 2 for stereo)

    # Create a BytesIO object to hold the WAV data in memory
    wav_data = io.BytesIO()

    # Create a new WAV file in memory
    with wave.open(wav_data, 'wb') as output_file:
        output_file.setnchannels(channels)
        output_file.setsampwidth(sample_width)
        output_file.setframerate(sample_rate)
        output_file.writeframes(audio_array)

    # Get the WAV data from the BytesIO object
    wav_data.seek(0)
    wav_bytes = wav_data.read()

    wav_bytes = trim_wav(wav_bytes, 10)  # eliminate noise

    return Response(wav_bytes, mimetype="audio/wav")


def trim_wav(wav_bytes: bytes, trim_ms: int):
    """Trim the first trim_ms of wav_bytes."""
    # Assuming `data` is your byte array containing the WAV data
    byte_stream = io.BytesIO(wav_bytes)

    # Load audio
    audio = AudioSegment.from_wav(byte_stream)

    # Return original wav if the duration is less than trim_ms 
    if audio.duration_seconds * 1000 <= trim_ms:
        return wav_bytes

    # Trim the first 3 seconds off
    audio = audio[trim_ms:]  # pydub works in milliseconds

    # If you want to save the result
    out_data = io.BytesIO()
    audio.export(out_data, format='wav')

    # Now out_data.getvalue() is your trimmed audio as bytes
    trimmed_audio_bytes = out_data.getvalue()

    return trimmed_audio_bytes
