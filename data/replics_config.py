START_REPLY = "юпи йоу юпи ей"
SET_START_COMMAND = "Начать работу"
FORWARD_REPLY = "Перешлите сообщение из канала, который хотите добавить"
ENTER_CHANNEL_ID = "Введите ID канала, который хотите удалить"
STATS_ALL_USERS = "Всего пользователей"
STATS_USERS = "пользователей"
ACCESS_DENIED = "Вы не администратор!"
CHANNEL_ADDED = "Канал успешно добавлен\nТеперь вы должны пригласить бота в канал."
ERROR = "Ошибка!"
CANCELED = "Отменено."
NEED_TO_FORWARD = "Перешлите сообщение из канала!"
CHANNEL_DELETED = "Канал успешно удален"
CHANNEL_DOESNT_EXIST = "Такого канала не существует."
ADD_APPROVED_ERROR = "Ошибка в добавлении принятого пользователя"
ADMIN_LIST = "Список админов"
ADMIN_ADD = "Перешлите сообщение пользователя, которого хотите сделать админом" \
            "\nИли отправьте его айди и никнейм в формате:\nuser_id username"
ADMIN_DEL = "Перешлите сообщение админа, которого хотите удалить" \
            "\nЛибо отправьте его айди"
NOT_COMMAND = "Я тебя не понял. Попробуй что-то из этой клавиатуры:"
# x - username ; y - user_id

ADMIN_SUCCESFULL_ADDED = lambda x: f"Админ {x} успешно добавлен"
ADMIN_SUCCESFULL_DELETED = lambda y: f"Админ {y} успешно удален"

# BUTTONS
# лучше не менять, иначе все поломается к хуям
# либо так же менять elif-ы в check_msg.py

ADD_CHANNEL_BUTTON = "Добавить канал"
DEL_CHANNEL_BUTTON = "Удалить канал"
STATS_BUTTON = "Статистика"
CANCEL_BUTTON = "Отмена"
ADMINS_BUTTON = "Админы"
ADD_ADMIN_BUTTON = "Добавить админа"
DEL_ADMIN_BUTTON = "Удалить админа"
