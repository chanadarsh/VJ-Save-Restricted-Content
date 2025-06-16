import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "10355467"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d86087c1892f818da03d68c3eaba765c")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "6073523936"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "postgresql://vjsavecontentbot_user:cCVkvxLKI3g4QztW3kdvkWuOhAkwDdnf@dpg-d17qembuibrs7380li6g-a.singapore-postgres.render.com/vjsavecontentbot") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
