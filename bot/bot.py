import sqlite3
import logging
from aiogram import Bot, Dispatcher, executor, types
API_TOKEN = '1974105410:AAEgB77ojFYxBhuvH_oz6y9qv7F2GOq7diw'
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
con = sqlite3.connect("../db.sqlite3")
cur = con.cursor()
@dp.message_handler()
async def echo(message: types.Message):
    USERID = message.chat.id
    USERNAME = message.chat.username
    CHECKUSER = False

    #START USER CHECK AUTH
    cur.execute(f"""
         SELECT userid FROM vote_botuser WHERE userid={USERID}
                """)
    result = cur.fetchall()
    if result == []:
        CHECKUSER = False
    else:
        CHECKUSER = True
    # END USER CHECK AUTH

    await message.reply("just")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
con.close()