import os
from typing import Set

from telethon.tl.types import ChatBannedRights
from validators.url import url


class Config(object):
    LOGGER = True
    
    ALIVE_NAME = os.environ.get("ALIVE_NAME", None)
    APP_ID = int(os.environ.get("APP_ID", 6))
    API_HASH = os.environ.get("API_HASH") or None
    DB_URI = os.environ.get("DATABASE_URL", None)
    STRING_SESSION = os.environ.get("STRING_SESSION", None)
    STRING_SESSION2 = os.environ.get("STRING_SESSION2", None)
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN") or os.environ.get(
        "TG_BOT_TOKEN_BF_HER", None
    )
    TG_BOT_USERNAME = None
    TZ = os.environ.get("TZ", "Asia/Baghdad")
    UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "https://github.com/ODY-IQ/CatArabic")
    EXTERNAL_REPO = os.environ.get("EXTERNAL_REPO", None)
    if bool(EXTERNAL_REPO and (EXTERNAL_REPO.lower() != "false")):
        if not url(EXTERNAL_REPO):
            EXTERNAL_REPO = ""
    else:
        EXTERNAL_REPO = None
    VCMODE = os.environ.get("VCMODE", False)
    PORT = os.environ.get("PORT", "8080")
    VCMODE = bool(VCMODE and (VCMODE.lower() != "false"))
    VC_SESSION = os.environ.get("VC_SESSION", None)
    ALIVE_PIC = os.environ.get("ALIVE_PIC", None)
    PING_TEXT = os.environ.get("PING_TEXT", None)
    ALIVE_MSG = os.environ.get("ALIVE_MSG", None)
    DEFAULT_BIO = os.environ.get("DEFAULT_BIO", None)
    PRIVATE_GROUP_BOT_API_ID = int(os.environ.get("PRIVATE_GROUP_BOT_API_ID") or 0)
    PRIVATE_GROUP_ID = int(os.environ.get("PRIVATE_GROUP_ID") or 0)
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    FBAN_GROUP_ID = int(os.environ.get("FBAN_GROUP_ID") or 0)
    PRIVATE_CHANNEL_BOT_API_ID = int(os.environ.get("PRIVATE_CHANNEL_BOT_API_ID") or 0)
    HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
    HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
    OWNER_ID = int(os.environ.get("OWNER_ID") or 0)
    PM_LOGGER_GROUP_ID = int(
        os.environ.get("PM_LOGGER_GROUP_ID")
        or os.environ.get("PM_LOGGR_BOT_API_ID")
        or 0
    )
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", None)
    TIME_JM = os.environ.get("TIME_JM", None)
    PLUGIN_CHANNEL = int(os.environ.get("PLUGIN_CHANNEL") or 0)
    TELEGRAPH_SHORT_NAME = os.environ.get("TELEGRAPH_SHORT_NAME", "jmthon")
    THUMB_IMAGE = os.environ.get(
        "THUMB_IMAGE", "https://telegra.ph/file/ca95524e4734b0d5461b5.jpg"
    )
    NO_LOAD = list(os.environ.get("NO_LOAD", "").split())
    TKRAR = os.environ.get("TKRAR", None)
    TI_FN = os.environ.get("TI_FN", None)

    COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r".")
    SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r".")
    TMP_DOWNLOAD_DIRECTORY = os.environ.get("TMP_DOWNLOAD_DIRECTORY", "downloads")
    TEMP_DIR = os.environ.get("TEMP_DIR", "./temp/")
    ANTISPAMBOT_BAN = os.environ.get("ANTISPAMBOT_BAN", False)
    FINISHED_PROGRESS_STR = os.environ.get("FINISHED_PROGRESS_STR", "▰")
    UNFINISHED_PROGRESS_STR = os.environ.get("UNFINISHED_PROGRESS_STR", "▱")
    SCREEN_SHOT_LAYER_ACCESS_KEY = os.environ.get("SCREEN_SHOT_LAYER_ACCESS_KEY", None)

    OPEN_WEATHER_MAP_APPID = os.environ.get("OPEN_WEATHER_MAP_APPID", None)
    IBM_WATSON_CRED_URL = os.environ.get("IBM_WATSON_CRED_URL", None)
    IBM_WATSON_CRED_PASSWORD = os.environ.get("IBM_WATSON_CRED_PASSWORD", None)
    IPDATA_API = os.environ.get("IPDATA_API", None)
    OCR_SPACE_API_KEY = os.environ.get("OCR_SPACE_API_KEY", None)
    GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None)
    REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", None)
    CURRENCY_API = os.environ.get("CURRENCY_API", None)
    G_DRIVE_CLIENT_ID = os.environ.get("G_DRIVE_CLIENT_ID", None)
    G_DRIVE_CLIENT_SECRET = os.environ.get("G_DRIVE_CLIENT_SECRET", None)
    G_DRIVE_FOLDER_ID = os.environ.get("G_DRIVE_FOLDER_ID", None)
    G_DRIVE_DATA = os.environ.get("G_DRIVE_DATA", None)
    G_DRIVE_INDEX_LINK = os.environ.get("G_DRIVE_INDEX_LINK", None)
    TG_2STEP_VERIFICATION_CODE = os.environ.get("TG_2STEP_VERIFICATION_CODE", None)
    WATCH_COUNTRY = os.environ.get("WATCH_COUNTRY", "IQ")
    BIO_PREFIX = os.environ.get("BIO_PREFIX", None)
    LASTFM_API = os.environ.get("LASTFM_API", None)
    LASTFM_SECRET = os.environ.get("LASTFM_SECRET", None)
    LASTFM_USERNAME = os.environ.get("LASTFM_USERNAME", None)
    LASTFM_PASSWORD_PLAIN = os.environ.get("LASTFM_PASSWORD", None)
    SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID", None)
    SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET", None)
    SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None)
    GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN", None)
    GIT_REPO_NAME = os.environ.get("GIT_REPO_NAME", None)

    DEEP_AI = os.environ.get("DEEP_AI", None)

    MAX_MESSAGE_SIZE_LIMIT = 4095
    LOAD = []
    ANTI_FLOOD_WARN_MODE = ChatBannedRights(
        until_date=None, view_messages=None, send_messages=True
    )
    CHROME_BIN = os.environ.get("CHROME_BIN", "/app/.apt/usr/bin/google-chrome")
    CHROME_DRIVER = os.environ.get(
        "CHROME_DRIVER", "/app/.chromedriver/bin/chromedriver"
    )
    GROUP_REG_SED_EX_BOT_S = os.environ.get(
        "GROUP_REG_SED_EX_BOT_S", r"(regex|moku|BananaButler_|rgx|l4mR)bot"
    )
    COUNTRY = str(os.environ.get("COUNTRY", ""))
    TZ_NUMBER = int(os.environ.get("TZ_NUMBER", 1))
    UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "master")
    SUDO_USERS: Set[int] = set()
    JMTHONUBLOGO = None
    BOTLOG = False
    BOTLOG_CHATID = 0
    EXTERNAL_REPOBRANCH = os.environ.get("EXTERNAL_REPOBRANCH", "main")


class Production(Config):
    LOGGER = False


class Development(Config):
    LOGGER = True
