#!/bin/bash

docker run --runtime=nvidia -p 8000:8000 -d -v /home/eden/projects/paddlespeech_docker:/paddle/paddlespeech paddlespeech:latest
