import sqlite3
import logging
import datetime
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
API_TOKEN = '1974105410:AAEgB77ojFYxBhuvH_oz6y9qv7F2GOq7diw'
# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage= MemoryStorage())
con = sqlite3.connect("../db.sqlite3",timeout=1)
cur = con.cursor()

class PhoneNumber(StatesGroup):
    step_1 = State()

@dp.message_handler()
async def alarm(message: types.Message):
    USERID = message.chat.id
    USERNAME = message.chat.username
    CHECKUSER = False

    cur.execute(f"""
             SELECT userid FROM vote_registredbotuser WHERE userid={USERID}
                    """)
    result = cur.fetchall()
    if result == []:
        CHECKUSER = False
    else:
        CHECKUSER = True


    if CHECKUSER == False:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        keyboard.add(types.KeyboardButton(text="Send ☎️", request_contact=True))
        await message.answer("Salom siz bu bo't orqalik Andijondagi eng yaxshi joylarga ovoz berishingiz mumkun bizga aniqlashga yordam bering siz ro'yhatdan o'tmagansiz iltimos ro'yhatdan o'tish uchun send tugmasini bosing", reply_markup=keyboard)
        await PhoneNumber.step_1.set()
    else:
        inline_btn_1 = types.InlineKeyboardButton(text="Ovoz berish 🎤️", callback_data='vote')
        inline_kb1 = types.InlineKeyboardMarkup().add(inline_btn_1)
        await message.reply(f"Salom siz bu bo't orqalik Andijondagi eng yaxshi joylarga ovoz berishingiz mumkun bizga aniqlashga yordam bering  ovoz berish uchun ovoz berish tugmasini bosing",reply_markup=inline_kb1)


@dp.message_handler(state=PhoneNumber.step_1, content_types=types.ContentTypes.CONTACT)
async def get_telephone_number(message: types.Message, state: FSMContext):
    userphonenumber = int(message.contact.phone_number)
    username = str(message.chat.username)
    userid = int(message.chat.id)
    cur.execute(f"""
                    INSERT INTO vote_registredbotuser(phone,userid,username)
                    VALUES
                    ({userphonenumber},{userid},'{username}');
                    """)
    con.commit()
    inline_btn_1 = types.InlineKeyboardButton(text="Ovoz berish 🎤️", callback_data='vote')
    inline_kb1 = types.InlineKeyboardMarkup().add(inline_btn_1)
    await message.reply(f"Muvofaqiyatlik ro'yhatdan o'tdingiz! ovoz berish uchun ovoz berish tugmasini bosing",reply_markup=inline_kb1)
    await state.finish()

@dp.callback_query_handler(lambda c: c.data == 'vote')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    category = cur.execute(f"""
                    SELECT name FROM vote_category
                """).fetchall()
    categorybtn = types.InlineKeyboardMarkup(row_width=2)
    for i in category:
        categorybtn.add(types.InlineKeyboardButton(f'{i[0]}', callback_data=f'for_category{i[0]}'))
    await bot.send_message(callback_query.from_user.id, "Iltimos kategoriyalardan tanlang",reply_markup=categorybtn)


@dp.callback_query_handler(lambda call:True)
async def process_callback_button(call: types.CallbackQuery):
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    if call.data.startswith("for_category"):
        categoryobj = cur.execute(f"""
                                            SELECT id FROM vote_category WHERE name="{call.data[12:]}"
                                            """).fetchall()

        placesobjs = cur.execute(f"""
                                        SELECT name FROM vote_places WHERE bind_id={categoryobj[0][0]}
                                        """).fetchall()

        for i in placesobjs:
            keyboard.add(types.InlineKeyboardButton(f'{i[0]} ⬆️', callback_data=f'for_places{i[0]}'))

        await bot.send_message(call.from_user.id, "Joy nomini tanlang va bosing",reply_markup=keyboard)

    if call.data.startswith("for_places"):
        placename = call.data[10:]
        dbplaces = cur.execute(f"""
                                    SELECT bind_id FROM vote_places WHERE name="{placename}"
                                """).fetchall()

        dbuser = cur.execute(f"""
                                  SELECT category_id FROM vote_botuser WHERE username="{call.from_user.username}"
                              """).fetchall()

        def incrandcreate():
            date = datetime.datetime.now().strftime("%Y-%m-%d")
            cur.execute(f"""
                            UPDATE vote_places SET vote = vote+1 WHERE name="{placename}"
                         """)
            userphonenumber = cur.execute(f"""
                                              SELECT phone FROM vote_registredbotuser WHERE username="{call.from_user.username}"
                                          """).fetchall()
            placesid = cur.execute(f"""
                                       SELECT * FROM vote_places WHERE name="{placename}"
                                    """).fetchall()

            categoryid = cur.execute(f"""
                                         SELECT id FROM vote_category WHERE id={placesid[0][4]}
                                     """).fetchall()
            cur.execute(f"""
                            INSERT INTO vote_botuser(phonenumber,userid,username,name,voted_id,category_id,date)
                            VALUES(
                                   {userphonenumber[0][0]},{call.from_user.id},"{call.from_user.username}","{call.from_user.first_name}",{placesid[0][0]},{categoryid[0][0]},"{date}"
                                   );

                         """)
            con.commit()

        if dbuser == []:
            incrandcreate()
            await bot.send_message(call.from_user.id,"Muvofaqiyatlik ovoz berdingiz fikringiz uchun rahmat!")
        else:
            if dbplaces[0][0] in [x[0] for x in dbuser]:
                votedpl = cur.execute(f"""
                                        SELECT bind_id FROM vote_places WHERE name="{placename}"
                                      """).fetchall()

                votedcategory = cur.execute(f"""
                                        SELECT name FROM vote_category WHERE id={votedpl[0][0]}
                                        """).fetchall()

                await bot.send_message(call.from_user.id, f"Siz oldin {votedcategory[0][0]}lardan biriga ovoz bergansiz iltimos boshqa kategoriya tanlab ovoz berin!")
            else:
                incrandcreate()
                await bot.send_message(call.from_user.id, "Muvofaqiyatlik ovoz berdingiz fikringiz uchun rahmat!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

con.close()
