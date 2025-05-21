from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils import executor

TOKEN = '8096490981:AAGxE5YFKqkKdZnNBUTRDdvgQSVcIaqj3Lo'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="Найти скидки рядом",
            web_app=WebAppInfo(url="https://ts-map.vercel.app/")
        )
    )
    await message.answer("Привет! Нажми кнопку ниже, чтобы открыть карту со скидками:", reply_markup=markup)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
