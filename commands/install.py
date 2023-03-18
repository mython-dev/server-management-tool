# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python

import subprocess
import os
from aiogram import types
from aiogram.types import ParseMode

# Данный код позволяет установить пакет на сервере Linux. 

async def install_command(message: types.Message):

    """
    Функция "installcommand" вызывает команду установки пакета в терминале через subprocess. 
    Переменная "packagename" содержит название пакета, который необходимо установить. 
    """

    try:
        package_name = message.text.split()[1]
        result = subprocess.check_output(["sudo", "apt", "install", "-y", package_name])
        await message.reply(f"Пакет {package_name} успешно установлен!\n", parse_mode=ParseMode.HTML)
    except Exception as e:
        await message.reply(f"Во время установки произошла ошибка: {str(e)}", parse_mode=ParseMode.HTML)
