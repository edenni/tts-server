FROM paddlepaddle/paddle:2.4.2-gpu-cuda11.7-cudnn8.4-trt8.4

RUN pip install paddlespeech pydub gunicorn flask

RUN mkdir -p /paddle/paddlespeech

WORKDIR /paddle/paddlespeech

ENTRYPOINT ["bash", "start_servers.sh"] 
