echo "Starting Legado HTTP server..."
gunicorn app:app -b 0.0.0.0:8000 --daemon
echo "Legago HTTP server started at port 8000"

echo "Starting PaddleSpeech server..."
paddlespeech_server start --config_file /paddle/paddlespeech/conf/tts.yaml
echo "Done"
