import logging
from aiogram import Bot, Dispatcher, executor, types
from vote.models import Category
API_TOKEN = '1974105410:AAEgB77ojFYxBhuvH_oz6y9qv7F2GOq7diw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):

    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)