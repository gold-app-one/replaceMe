import os
from customTypes.path import Path


ROOT_PATH: Path = Path(os.path.split(os.path.abspath(__file__))[0])
DATA_PATH: Path = ROOT_PATH + 'data'
WHATSAPP_PATH: Path = DATA_PATH + 'whatsapp'
WHATSAPP_CHATS_PATH: Path = WHATSAPP_PATH + 'chats'