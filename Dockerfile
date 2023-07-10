FROM paddlepaddle/paddle:2.4.2-gpu-cuda11.7-cudnn8.4-trt8.4

RUN mkdir -p /paddle/paddlespeech

WORKDIR /paddle/paddlespeech

COPY . .
RUN pip install -r requirements.txt

RUN python download_models.py

ENTRYPOINT ["bash", "start_servers.sh"] 
