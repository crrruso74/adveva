import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'AM_ROBOTS')
API_ID = int(environ.get('API_ID', '24281454'))
API_HASH = environ.get('API_HASH', 'dbe4521b4291da85becb65c7d4d4c36c')
BOT_TOKEN = environ.get('BOT_TOKEN', '5329268513:AAGEjMSvnN7LOMor7p9FIQmjnMa18CZIkyo')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
PICS = (environ.get('PICS', 'https://telegra.ph/file/b3382933128d32f5ed636.jpg https://telegra.ph/file/a0289dc1f4760264a52c3.jpg https://telegra.ph/file/eb425f69630fcfa07b339.jpg https://telegra.ph/file/596bfa56b8c69f356cd84.jpg https://telegra.ph/file/5b4fd15fdabc5057489ef.jpg https://telegra.ph/file/5ab1105bb33d928af1384.jpg https://telegra.ph/file/78014866e4f90fc8ae055.jpg https://telegra.ph/file/ab1c61e23ade815a3b54e.jpg https://telegra.ph/file/25f236b9e699d3928bcc9.jpg https://telegra.ph/file/81748dcb455c013ff59d4.jpg https://telegra.ph/file/ab43ae8c5b1d82dce0882.jpg https://telegra.ph/file/8326290311c5cc28f497a.jpg https://telegra.ph/file/66c4ed7c573b9ff6888f5.jpg https://telegra.ph/file/3d22394d3b427db3be1ef.jpg https://telegra.ph/file/6f615e5a6fd75f3e1befb.jpg https://telegra.ph/file/90a37d031c84d6698cf39.jpg https://telegra.ph/file/8ee48d027364a28ec3998.jpg https://telegra.ph/file/5d07381296cf40936bcca.jpg https://telegra.ph/file/6303bc63d06c76451bcc9.jpg https://telegra.ph/file/ead66627b65f07b812e6e.jpg')).split()

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5650200786').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001868456119').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5650200786').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb://movie:movie@ac-xsggctk-shard-00-00.regyvfx.mongodb.net:27017,ac-xsggctk-shard-00-01.regyvfx.mongodb.net:27017,ac-xsggctk-shard-00-02.regyvfx.mongodb.net:27017/?ssl=true&replicaSet=atlas-de7prp-shard-0&authSource=admin&retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "papkarn")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001889413006'))
SUPPORT_CHAT = environ.get('GROUP', 'MX_Movie_Request')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), False)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "<b><i>{file_name} » {file_size}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", "<b><i>{file_name} » {file_size}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> \n🔮 𝖸𝖾𝖺𝗋: {year} \n⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10 \n🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} \n\n🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [MX Networks]")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), True)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001868456119')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "False")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"

## EXTRA FEATURES ##

     # Auto Delete For Group Message (Self Delete) #
SELF_DELETE_SECONDS = int(environ.get('SELF_DELETE_SECONDS', 160))
SELF_DELETE = environ.get('SELF_DELETE', True)
if SELF_DELETE == "True":
    SELF_DELETE = True
