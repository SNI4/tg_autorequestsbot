from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.replics_config import ADD_ADMIN_BUTTON, DEL_ADMIN_BUTTON


def admin_reply_keyboard() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    ib1 = KeyboardButton(text=ADD_ADMIN_BUTTON)
    ib2 = KeyboardButton(text=DEL_ADMIN_BUTTON)

    return ikb.row(ib1, ib2)
