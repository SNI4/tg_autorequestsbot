from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from data.replics_config import *
from keyboards.admin_actions_keyboard import admin_reply_keyboard
from keyboards.base_reply import base_reply_keyboard
from keyboards.cancel import cancel_keyboard
from loader import dp
from utils.misc.json_admins_worker import *
from utils.misc.json_channels_worker import *


class FSM(StatesGroup):
    channel_id_add = State()
    channel_id_del = State()
    admin_add = State()
    admin_del = State()


@dp.message_handler()
async def check(message: types.Message):
    if str(message.from_id) not in (await get_admins()).keys():
        m = message.text.lower()

        if message.forward_from_chat:
            await message.reply(
                f"ID Канала: {message.forward_from_chat.id}\nИмя канала: {message.forward_from_chat.title}")

        elif m == "добавить канал":
            await FSM.channel_id_add.set()
            await message.reply(FORWARD_REPLY, reply_markup=cancel_keyboard())

        elif m == "удалить канал":
            await FSM.channel_id_del.set()
            await message.reply(ENTER_CHANNEL_ID, reply_markup=cancel_keyboard())

        elif m == "статистика":
            data = await get_channels()
            sum_users = 0
            mes = '\n'.join([f"{data[key]['channel_name']} ({key}): {str(data[key]['users'])} {STATS_USERS}" for key in
                             data.keys()])

            for key in data.keys():
                sum_users += data[key]['users']

            await message.reply(f"{STATS_ALL_USERS}: {str(sum_users)}\n\n{mes}")

        elif m == "админы":
            data = await get_admins()
            mes = f'{ADMIN_LIST}:\n' + '\n'.join([f"{data[key]} ({key})" for key in data.keys()])
            await message.reply(mes, reply_markup=admin_reply_keyboard())

        elif m == "добавить админа":
            await FSM.admin_add.set()
            await message.reply(ADMIN_ADD, reply_markup=cancel_keyboard())

        elif m == "удалить админа":
            await FSM.admin_del.set()
            await message.reply(ADMIN_DEL, reply_markup=cancel_keyboard())

        else:
            await message.reply(NOT_COMMAND, reply_markup=base_reply_keyboard())
    else:
        await message.reply(ACCESS_DENIED)


@dp.message_handler(state=FSM.channel_id_add)
async def save_channel(message: types.Message, state=FSMContext):
    if message.forward_from_chat:
        add = await add_channel(str(message.forward_from_chat.id), str(message.forward_from_chat.title))
        if add:
            await message.reply(CHANNEL_ADDED,
                                reply_markup=base_reply_keyboard())
            await state.finish()
        else:
            await message.reply(f"{ERROR}\n{add}")

    elif message.text.lower() == "отмена":
        await state.finish()
        await message.reply(CANCELED, reply_markup=base_reply_keyboard())

    else:
        await message.reply(NEED_TO_FORWARD, reply_markup=cancel_keyboard())


@dp.message_handler(state=FSM.channel_id_del)
async def delete_channel(message: types.Message, state=FSMContext):
    if message.text != "Отмена":
        action = await del_channel(message.text)
        if action:
            await message.reply(CHANNEL_DELETED, reply_markup=base_reply_keyboard())
        else:
            await message.reply(CHANNEL_DOESNT_EXIST, reply_markup=cancel_keyboard())

    else:
        await message.reply(CANCELED, reply_markup=base_reply_keyboard())

    await state.finish()


@dp.message_handler(state=FSM.admin_add)
async def add_admin_action(message: types.Message, state=FSMContext):
    if message.text.lower() != "отмена":
        try:
            if message.is_forward():
                user_id = str(message.forward_from.id)
                username = message.forward_from.username

            else:
                user_id = message.text.split()[0]
                username = message.text.split()[1]

            if user_id != str(ADMIN_ID):
                action = await add_admin(user_id, username)

                if action:
                    await message.reply(ADMIN_SUCCESFULL_ADDED(username), reply_markup=base_reply_keyboard())

                else:
                    await message.reply(ERROR + action, reply_markup=base_reply_keyboard())

                await state.finish()

            else:
                await state.finish()
                await message.reply(CANCELED, reply_markup=base_reply_keyboard())

        except IndexError:
            await message.reply(ADMIN_ADD, reply_markup=cancel_keyboard())
    else:
        await state.finish()
        await message.reply(CANCELED, reply_markup=base_reply_keyboard())


@dp.message_handler(state=FSM.admin_del)
async def del_admin_action(message: types.Message, state=FSMContext):
    if message.text.lower() != "отмена":
        user_id = str(message.forward_from.id) if message.is_forward() else message.text

        if (user_id != str(ADMIN_ID)) and (user_id in (await get_admins()).keys()):
            action = await del_admin(user_id)

            if action:
                await message.reply(ADMIN_SUCCESFULL_DELETED(user_id), reply_markup=base_reply_keyboard())

            else:
                await message.reply(ERROR + action, reply_markup=base_reply_keyboard())

            await state.finish()

        else:
            await state.finish()
            await message.reply(CANCELED, reply_markup=base_reply_keyboard())

    else:
        await state.finish()
        await message.reply(CANCELED, reply_markup=base_reply_keyboard())
