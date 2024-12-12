from aiogram import types, Bot, Dispatcher
from aiogram.filters import CommandStart
import asyncio
token = '6544378792:AAECxNNe0RZy2A0RKfJRN0lu9Jis-AktKN4'
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(CommandStart())
async def get_start(msg: types.Message):
    await msg.answer(text="Assalamu Aleykum")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())