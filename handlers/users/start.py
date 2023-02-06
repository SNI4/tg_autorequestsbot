from aiogram import types

from keyboards.base_reply import base_reply_keyboard
from loader import dp


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer('юпи йоу юпи ей', reply_markup=base_reply_keyboard())
