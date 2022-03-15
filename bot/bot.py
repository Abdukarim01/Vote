import os
import logging
from pathlib import Path
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'configs.settings')
django.setup()
from aiogram import Bot, Dispatcher, executor, types
logging.basicConfig(level=logging.INFO)
BOT_TOKEN = "1974105410:AAEgB77ojFYxBhuvH_oz6y9qv7F2GOq7diw"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


from vote.models import Category
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
