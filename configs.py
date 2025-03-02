

from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "26514205"))
    API_HASH = getenv("API_HASH", "c96b468c5a2bdcfdf92cbc2f9d87f00f")
    BOT_TOKEN = getenv("BOT_TOKEN", "7945819267:AAG_v2bPJA_3QminolkFC9Lrs-nNf7g2f48")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002422827624")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "7130114315").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://bot:bot@cluster0.8vepzds.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

