from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from data.config import ADMIN_ID
from keyboards.base_reply import base_reply_keyboard
from keyboards.cancel import cancel_keyboard
from loader import dp
from utils.misc.json_channels_worker import add_channel, get_channels, del_channel


class FSM(StatesGroup):
    channel_id_add = State()
    channel_id_del = State()


@dp.message_handler()
async def check(message: types.Message):
    if message.from_id == ADMIN_ID:
        if message.forward_from_chat:
            await message.reply(
                f"ID Канала: {message.forward_from_chat.id}\nИмя канала: {message.forward_from_chat.title}")

        elif message.text == "Добавить канал":
            await FSM.channel_id_add.set()
            await message.reply("Перешлите сообщение из канала, который хотите добавить", reply_markup=cancel_keyboard())

        elif message.text == "Удалить канал":
            await FSM.channel_id_del.set()
            await message.reply("Введите ID канала, который хотите удалить", reply_markup=cancel_keyboard())

        elif message.text == "Статистика":
            data = await get_channels()
            sum_users = 0
            mes = '\n'.join([f"{data[key]['channel_name']}: {str(data[key]['users'])} пользователей" for key in data.keys()])

            for key in data.keys():
                sum_users += data[key]['users']

            await message.reply(f"Всего пользователей: {str(sum_users)}\n\n{mes}")

    else:
        await message.reply("Вы не администратор!")


@dp.message_handler(state=FSM.channel_id_add)
async def save_channel(message: types.Message, state=FSMContext):
    if message.forward_from_chat:
        add = await add_channel(str(message.forward_from_chat.id), str(message.forward_from_chat.title))
        if add:
            await message.reply("Канал успешно добавлен\nТеперь вы должны пригласить бота в канал.",
                                reply_markup=base_reply_keyboard())
            await state.finish()
        else:
            await message.reply(f"Ошибка!\n{add}")

    elif message.text == "Отмена":
        await state.finish()
        await message.reply("Отменено.", reply_markup=base_reply_keyboard())

    else:
        await message.reply("Перешлите сообщение из канала!", reply_markup=cancel_keyboard())


@dp.message_handler(state=FSM.channel_id_del)
async def delete_channel(message: types.Message, state=FSMContext):
    if message.text != "Отмена":
        action = await del_channel(message.text)
        if action:
            await message.reply("Канал успешно удален", reply_markup=base_reply_keyboard())
            await state.finish()
        else:
            await message.reply("Такого канала не существует.", reply_markup=cancel_keyboard())

    else:
        await state.finish()
        await message.reply("Отменено.", reply_markup=base_reply_keyboard())
