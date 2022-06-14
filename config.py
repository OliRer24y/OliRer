## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgCdJnKeH1ggSgV6Bx5AzcIMCmhkbwstSJs3kjUS9ACiQrtZ2UTXgV6WR9yUfriSy8ltz8MVWT6zpQd1jHV6tgKegLWyGSdixjXXpQ9te1tMkK-cNkdqD3v65D2c_Q_oE5EDA021Bw9X9h2ODRyOz0ZNhfWzSGolEL-kiec7YiPVumA-d9A7XsyqYXjwGZM-TNU1-0akzTTtAdMiCjUtwiOSceJhfo5GzHcrJuG0XCFIdJHcDiclrQIpNcCh4I1tZrnV-x8wNseeZF6MaBKuXk-1_ta5VuOO-L7fyw6GAktAM0B1YQfOK6LdFyvwLypSBUZkUecLl8dEsFz6-Oy2_gRGAAAAATd0tfgA")
BOT_TOKEN = getenv("BOT_TOKEN", "5576140304:AAEDh5rSs6ht-6S-pUW_fU3udTkSjn1wJtg")
BOT_NAME = getenv("BOT_NAME", "𝚖𝚞𝚜𝚒𝚌 𝚋𝚘𝚝 ⁦.")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "muntazer")
OWNER_USERNAME = getenv("OWNER_USERNAME", "ZZZZ8lZ")
ALIVE_NAME = getenv("ALIVE_NAME", "muntazer")
BOT_USERNAME = getenv("BOT_USERNAME", "G_12_BOT")
OWNER_ID = getenv("OWNER_ID", "1892734080")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Se_fm")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "ZZZZ8lZ")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1892734080").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/46fa55b49b85c084159ce.png")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/466de30ee0f9383c8e09e.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/46fa55b49b85c084159ce.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/a282c460a7f98aedbe956.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/8fe190a2a52986bd29dc5.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
