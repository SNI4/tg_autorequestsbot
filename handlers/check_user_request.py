from aiogram import types
from data.replics_config import ADD_APPROVED_ERROR
from data.config import ADMIN_ID
from loader import dp, bot
from utils.misc.json_channels_worker import add_approved


@dp.chat_join_request_handler()
async def approve(update: types.ChatJoinRequest):
    await update.approve()

    add_approve = await add_approved(str(update.chat.id))

    if add_approve:
        pass
    else:
        bot.send_message(ADMIN_ID, f"{ADD_APPROVED_ERROR}:\n{add_approved}")

