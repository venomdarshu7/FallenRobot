class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 20738979
    API_HASH = "a6d015153068a35390a336fe0a38dd64"

    CASH_API_KEY = "EWW2T30R2NSCYVC8"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://euacssdp:ExVTYiLLq8fEtG6vkTNO805DrYdbSjn9@jelani.db.elephantsql.com/euacssdp"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001586622410)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://das:darshu567@cluster0.mwgkkci.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/a1489375c10e1f70156e0.jpg"

    SUPPORT_CHAT = "vdsamr"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6472392988:AAGczAHFlx_U2Fh-LkzrjMT6sGJCniCSWwA"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "http://api.timezonedb.com/v2.1/list-time-zone"  # Get this value from https://timezonedb.com/api

    OWNER_ID = "5658395021"  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
