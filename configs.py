# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "26514205"))
    API_HASH = getenv("API_HASH", "c96b468c5a2bdcfdf92cbc2f9d87f00f")
    BOT_TOKEN = getenv("BOT_TOKEN", "7364219421:AAEHk9QDXMrDicEWHt4fN7OeLhUJf-10Nm0")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002452035488")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "7130114315").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://bot:bot@cluster0.8vepzds.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
