from aiogram import types
from data.replics_config import START_REPLY
from keyboards.base_reply import base_reply_keyboard
from loader import dp


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(START_REPLY, reply_markup=base_reply_keyboard())
