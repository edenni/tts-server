# A TTS-Server powered by vits

`python=3.7`

Original repo: https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/tree/main

Pre-trained model: https://huggingface.co/spaces/sayashi/vits-uma-genshin-honkai/blob/main/model/G_953000.pth

Start server with `server.py`.

## Using with Legado

Create a new tts setting. Set `url` as 

```
<YOUR_SERVER_HOST>:<PORT>/tts, {"method", "POST", "body": {"text": "{{speakText}}"}}
```

See [this](https://github.com/gedoor/legado/blob/203de9f0543d198e286d5903d570054e0a3ba409/app/src/main/assets/defaultData/httpTTS.json) for templates.
