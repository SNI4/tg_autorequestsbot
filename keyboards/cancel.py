from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def cancel_keyboard() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    ib1 = KeyboardButton(text="Отмена")

    return ikb.add(ib1)
