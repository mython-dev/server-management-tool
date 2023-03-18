# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python


# Данный код позволяет удалить пакет на сервере Linux. 

from aiogram import types
from aiogram.types import ParseMode
import subprocess

async def remove_command(message: types.Message):

    """
    Функция "remove_command"
    вызывает команду удаления пакета в терминале через subprocess. 
    Если удаление прошло успешно, бот отправляет сообщение о том, что пакет успешно удален. 
    Если произошла ошибка, сообщение содержит информацию об ошибке. 
    """

    package_name = message.text.split(' ')[1] # Переменная "packagename" содержит название пакета, который необходимо удалить. 
    try:
        subprocess.check_call(['sudo', 'apt', 'remove', '-y', package_name])
        await message.reply(f'Пакет {package_name} успешно удален', parse_mode=ParseMode.HTML)
    except subprocess.CalledProcessError as e:
        await message.reply(f'Произошла ошибка при удалении пакета {package_name}: {e}', parse_mode=ParseMode.HTML)

