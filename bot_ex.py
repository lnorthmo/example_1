import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from db_conn import set_state, get_state


API_TOKEN = 'ur_token'
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands="check")
async def check(message: types.Message):
    await set_state(message.chat.id, "Ex_state")
    await message.reply("пиши что либо")


@dp.message_handler(state='*')  # работает все время, и когда что то пользователь что то делает проверяет поменлось ли его состояние
async def process_message(message: types.Message):
    state = await get_state(message.chat.id)  # получение состояния пользователя которые мы ему сами задали
    await set_state(message.chat.id, None)  # обнулениче состояния
    if state == 'ex_state':
        chat_id = message.chat.id

        data = message.text  # здесь цепляешь сообщение

        text = "с этого id {} пришел такой текст {}".format(chat_id, data)

        await bot.send_message("ur_chat_id", text)  # здесь отправляешь
