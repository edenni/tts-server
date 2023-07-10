# TTS Server

A PaddleSpeech powered TTS server for Legado.

## TODO

- [x] Use Unicorn instead of the development HTTP server

- [x] Download necessary models when building image

- [ ] Fine-tune the pre-trained model with a [custom dataset](https://github.com/w4123/GenshinVoice)
  - [ ] Learn about some model details
  - [ ] Prepare the dataset for fine-tuning
  - [ ] Training  

## Build Docker image & start container
```
bash build_image.sh

bash run.sh
```

## Using with Legado

Create a new tts setting. Set `url` as 

```
<YOUR_SERVER_HOST>:<PORT>/tts, {"method", "POST", "body": {"text": "{{speakText}}"}}
```

See [this](https://github.com/gedoor/legado/blob/203de9f0543d198e286d5903d570054e0a3ba409/app/src/main/assets/defaultData/httpTTS.json) for templates.

