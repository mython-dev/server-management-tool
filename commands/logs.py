# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python


import os
from aiogram import types

import aiogram
from config import BOT_TOKEN, TELEGRAM_ID

bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.Dispatcher(bot)


async def send_logs(message: types.Message):
    # путь к каталогу с файлами
    directory = "/var/log/"
    # получаем список файлов в каталоге
    files = os.listdir(directory)

    logs = {
        "syslog": "/var/log/syslog - системный журнал, который содержит информацию о работе ядра, демонов и сервисов.",
        "auth.log": "/var/log/auth.log - журнал аутентификации, который содержит информацию обо всех попытках входа в систему, изменениях прав пользователей и других событиях, связанных с безопасностью.",
        "kern.log": "/var/log/kern.log - журнал ядра, который содержит информацию о работе ядра операционной системы, такую как сообщения об ошибках, предупреждения и другие события.",
        "messages": "/var/log/messages - общий журнал системы, который содержит информацию о работе всех сервисов и демонов, а также сообщения об ошибках и предупреждения.",
        "daemon.log": "/var/log/daemon.log - журнал демонов, который содержит информацию о работе всех системных демонов, таких как Apache, MySQL и других сервисов.",
        "apache2/error.log": "/var/log/apache2/error.log - журнал ошибок Apache2, который содержит информацию о возникших ошибках веб-сервера Apache2.",
        "nginx/error.log": "/var/log/nginx/error.log - журнал ошибок Nginx, который содержит информацию о возникших ошибках веб-сервера Nginx. " 
    }

    for log_file, caption in logs.items():
        try:
            if os.path.exists(directory + log_file):
                with open(os.path.join(directory + log_file), "rb") as f:
                    await bot.send_document(chat_id=TELEGRAM_ID, document=f, caption=caption)
            else:
                await message.reply(f'Не получилось отправить лог: "{log_file}"!')
        except Exception as e:
            await message.reply(f'Произошла ошибка при отправке лога "{log_file}": {e}')