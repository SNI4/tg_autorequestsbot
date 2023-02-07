from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.replics_config import CANCEL_BUTTON


def cancel_keyboard() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    ib1 = KeyboardButton(text=CANCEL_BUTTON)

    return ikb.add(ib1)
