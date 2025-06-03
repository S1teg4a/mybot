import os
from dotenv import load_dotenv

load_dotenv(".env")

MAX_BOT = int(os.getenv("MAX_BOT", "200"))

DEVS = list(map(int, os.getenv("DEVS", "5716598718").split()))

API_ID = int(os.getenv("API_ID", "22550997"))

API_HASH = os.getenv("API_HASH", "90aa08d2d7217fbfd511cdff22530fb5")

BOT_TOKEN = os.getenv("BOT_TOKEN", "7915569165:AAF975EB35V9bFkiTP71XN7Q_pGzOk_wkS8
")

OWNER_ID = int(os.getenv("OWNER_ID", "5716598718"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002125842026 -1002053287763 -1002694842430 -1002022625433 -1002050846285 -1002400165299 -1002416419679 -1001473548283").split()))

RMBG_API = os.getenv("RMBG_API", "a6qxsmMJ3CsNo7HyxuKGsP1o")

MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://ranggadtya35:nUGXUW50EB3sT97j@cluster0.caxg2rg.mongodb.net/")

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002694842430"))

