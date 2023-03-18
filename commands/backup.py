# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python

import datetime
import subprocess
from bot import *


async def backup_command(message: types.Message):

    """
    Функция backup_command принимает объект сообщения типа Message из библиотеки aiogram. 
    Функция выполняет создание резервной копии файловой системы с помощью команды tar в терминале. 
    """

    try:
        # Разделяет текст сообщения на слова и сохраняет их в переменную words.
        words = message.text.split()

        # Если количество слов больше двух, то:
        if len(words) > 2:

            # Сохраняет путь для архивирования и путь для сохранения резервной копии в переменные backup_path и save_to_backup соответственно.    
            save_to_backup, backup_path = words[2], words[1]

            # Получает текущую дату и время в формате "%Y-%m-%d_%H:%M:%S" и сохраняет в переменную date.
            date = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

            # задаем имя архива и путь к папке для архивирования
            backup_name = f"{save_to_backup}{date}.tar.gz"

            # формируем команду для создания архива
            command = f"tar -czvf {backup_name} {backup_path}"

            # запускаем команду в терминале
            subprocess.run(command, shell=True)

            # Отправляет ответ пользователю о успешном создании резервной копии с указанием пути к файлу.
            await message.reply(f'Успешно сделан backup путь: {backup_name}')

        # Если количество слов меньше или равно двум, то отправляет пользователю сообщение с просьбой ввести путь для архивирования и путь для сохранения резервной копии.
        else:
            await message.answer("Введите путь: /backup /make/backup/in/this/path /save/in/this/path")

    except Exception as e: # Если произошла какая-либо ошибка, то отправляет пользователю сообщение с указанием ошибки.
        await message.answer(f"Произошла ошибка: {e}")
