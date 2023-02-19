import json
from flask import Flask, Response, request
from app import vits, search_speaker, speakers
import io
import numpy as np
from scipy.io.wavfile import write

app = Flask(__name__)

lang = 0
speaker_id = 190  # hanser
ns, nsw, ls = 0.6, 0.668, 1.2  # 感情变化, 音素发音长度, 整体语速


@app.route("/tts", methods=["GET", "POST"])
def streamwav():
    data = json.loads(str(request.data, encoding="utf-8"))
    text = data["text"]

    def generate(text):
        _, (sr, audio), _ = vits(text, lang, speaker_id, ns, nsw, ls)

        bytes_wav = bytes()
        byte_io = io.BytesIO(bytes_wav)
        write(byte_io, sr, audio)
        yield byte_io.read()

    return Response(generate(text), mimetype="audio/wav")