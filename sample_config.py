import os

from dotenv import load_dotenv

load_dotenv(
    "config.env" if os.path.isfile("config.env") else "sample_config.env"
)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6652148246:AAFW45QJL95sK9DywEHzm7DaY4LIpQc76bE")
API_ID = int(os.environ.get("API_ID", "22514909"))
SESSION_STRING = os.environ.get("SESSION_STRING", "AgFXjN0AtAUKvmL9S4q0FPsekOz0Kro_o5Va_awK8wNPoWiZAfzO23wfgV-NZo4AY7bZ_ojmNigZ-LWOrbbYcUWCTuyvc8QWDZ8mYaC4V3tVhnV3OizTzGooBKcXrnydyRv9_72okkmSOd9MyOV1DTAE32VXXu1wgtHwgW8VwOBVd527mYaWexwBkth4n4fsfMoc-rsWjvPKrXV-ip5fJgYgMZsx5zs6WyR0my_gTjhzSOL3Y3Rk6IyTE7auOUClLU8zSuku5KEzUN-rL5czTerDL9fQ0-ESeskmRbHa-6XEsdCk4YoqQcRRtT2JI86nL0L06DfnJsXQvpHT5Tetdsak0KhOZwAAAAF8uz0RAA")
API_HASH = os.environ.get("API_HASH","625b2dfe66926aaf7a41018d07eba8a7")
USERBOT_PREFIX = os.environ.get("USERBOT_PREFIX", "repotestbot")
PHONE_NUMBER = os.environ.get("PHONE_NUMBER","+994512013527")
SUDO_USERS_ID = list(map(int, os.environ.get("SUDO_USERS_ID", "5570119623 5045429385").split()))
LOG_GROUP_ID = int(os.environ.get("LOG_GROUP_ID", "-1001609611579"))
GBAN_LOG_GROUP_ID = int(os.environ.get("GBAN_LOG_GROUP_ID","-1001674865910"))
MESSAGE_DUMP_CHAT = int(os.environ.get("MESSAGE_DUMP_CHAT","neonfedsupport"))
WELCOME_DELAY_KICK_SEC = int(os.environ.get("WELCOME_DELAY_KICK_SEC", 600))
MONGO_URL = os.environ.get("MONGO_URL","mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority")
ARQ_API_KEY = os.environ.get("ARQ_API_KEY")
ARQ_API_URL = os.environ.get("ARQ_API_URL", "https://arq.hamker.dev")
LOG_MENTIONS = os.environ.get("LOG_MENTIONS", "True").lower() in ["true", "1"]
RSS_DELAY = int(os.environ.get("RSS_DELAY", 300))
PM_PERMIT = os.environ.get("PM_PERMIT", "True").lower() in ["true", "1"]
