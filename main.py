from aiogram import Bot, Dispatcher
from aiogram.types import Message

from config import TOKEN_API

bot = Bot(token=TOKEN_API)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: Message):
    await message.reply('Привет! Я умный калькулятор! Чтобы начать, введите ваше выражение.')

@dp.message_handler(commands=['help'])
async def send_help(message: Message):
    await message.reply('Я понимаю следующие операции: сложение (+), вычитание (-), умножение (*), деление (/).')

@dp.message_handler()
async def calculate(message: Message):
    expression = message.text
    try:
        result = eval(expression)
    except:
        await message.reply("Некорректное ввод! Пожалуйста, попробуйте еще раз.")
    else:
        await message.reply(f"Результат: {result}")