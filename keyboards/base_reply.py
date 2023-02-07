from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from data.replics_config import ADD_CHANNEL_BUTTON, DEL_CHANNEL_BUTTON, STATS_BUTTON, ADMINS_BUTTON


def base_reply_keyboard() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    ib1 = KeyboardButton(text=ADD_CHANNEL_BUTTON)
    ib2 = KeyboardButton(text=DEL_CHANNEL_BUTTON)
    ib3 = KeyboardButton(text=STATS_BUTTON)
    ib4 = KeyboardButton(text=ADMINS_BUTTON)

    return ikb.row(ib1, ib2).add(ib3).add(ib4)
