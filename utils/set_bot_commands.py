from aiogram import types
from data.replics_config import SET_START_COMMAND


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", SET_START_COMMAND)
        ]
    )
