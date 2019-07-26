from aiogram import types

from core.config import author
from core.misc import bot, dp


@dp.message_handler(lambda m: m.from_user.username == author, commands=['test'])
async def cmd_test(m):
    await bot.delete_message(m.chat.id, m.message_id)


# @dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply('I will delete your message')
    await bot.delete_message(message.chat.id, message.message_id)
