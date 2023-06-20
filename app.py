from aiogram import *
from aiogram.types.web_app_info import WebAppInfo

import json

bot = Bot('5557001381:AAHx607vVDAmcODIHuBav4FKZ-Zp0sFTTLk')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open Web App', web_app=WebAppInfo(url='https://salohiddinusmonaliyev.github.io/webapp/')))

    await message.answer("Hello", reply_markup=markup)

@dp.message_handler(content_types=['web_app_data'])
async def web_app(message: types.Message):
    myjson = json.loads(message.web_app_data.data)
    await message.answer(f"First name: {myjson['first_name']} \nLast name: {myjson['last_name']} \nPhone number: {myjson['phone_number']} \nQuantity: {myjson['quantity']}")

executor.start_polling(dp)