from aiogram import types
from core.misc import dp
from core.localisation import _


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    print('START COMMAND')
    # NOTE: This is a test translation. For more info visit: https://github.com/aiogram/aiogram/blob/dev-2.x/examples/i18n_example.py
    await message.reply(_('Hi!!'))
