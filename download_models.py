from paddlespeech.server.engine.engine_pool import init_engine_pool
from paddlespeech.server.utils.config import get_config

config = get_config("conf/tts.yaml")
init_engine_pool(config)
