# Don't Remove Credit Tg - @VJ_Bots
# Subscribe YouTube Channel For Amazing Bot https://youtube.com/@Tech_VJ
# Ask Doubt on telegram @KingVJ01

import os

# Login feature, if you want then True , if you don't want then False
def env_bool(name, default=True):
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {'1', 'true', 'yes', 'y', 'on'}

LOGIN_SYSTEM = env_bool('LOGIN_SYSTEM', True)

if LOGIN_SYSTEM == False:
    # if login system is False then fill your tg account session below 
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
else:
    STRING_SESSION = None

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8855925169:AAH6CNpFlY7dlTR5GWpRMx1TMSnY5o1x-ds")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "34338736"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "cb0624172e5db326489e1855a83d0c26")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8606649929"))

# Your Channel Id In Which Bot Upload Downloaded Video/File/Message etc.
# And Make Your Bot Admin In this channel with full rights.
# if you don't want to upload in channel then leave it blank don't fill anything.
CHANNEL_ID = os.environ.get("CHANNEL_ID", "")

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://DemoArjun:0JGyLYySiCNxBmuW@cluster0.nln6lwr.mongodb.net/?appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "DemoArjun")

# Increase time as much as possible to avoid floodwait, spamming and tg account ban issues.
WAITING_TIME = int(os.environ.get("WAITING_TIME", "10")) # time in seconds

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = env_bool('ERROR_MESSAGE', True)
