# TTS Server

A PaddleSpeech powered TTS server for Legado.

## TODO

- [x] Use Unicorn instead of the development HTTP server

- [ ] Download necessary models when building image

- [ ] Fine-tune the pre-trained model with a [custom dataset](https://github.com/w4123/GenshinVoice)

## Start Docker

```
docker build . -t paddlespeech

docker run --runtime=nvidia -p 5000:5000 -it paddlespeech:latest
```

## Using with Legado

Create a new tts setting. Set `url` as 

```
<YOUR_SERVER_HOST>:<PORT>/tts, {"method", "POST", "body": {"text": "{{speakText}}"}}
```

See [this](https://github.com/gedoor/legado/blob/203de9f0543d198e286d5903d570054e0a3ba409/app/src/main/assets/defaultData/httpTTS.json) for templates.

