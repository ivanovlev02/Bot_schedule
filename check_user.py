
TOKEN = ""
USER_ID = ""

import telepot
from telepot.loop import MessageLoop

bot = telepot.Bot(TOKEN)
info = bot.getChat(USER_ID)
print(info)
