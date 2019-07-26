from aiogram import types
from core.misc import dp


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    print('START COMMAND')
    await message.reply('Hi!!')
