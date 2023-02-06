from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def base_reply_keyboard() -> ReplyKeyboardMarkup:
    ikb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

    ib1 = KeyboardButton(text="Добавить канал")
    ib2 = KeyboardButton(text="Удалить канал")
    ib3 = KeyboardButton(text="Статистика")

    return ikb.add(ib1).row(ib2, ib3)
