# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python

import subprocess
from aiogram import types

try:
    async def date_command(message: types.Message):

        """
        Функция date_command предназначена для получения текущей даты и времени на сервере, 
        на котором запущен бот. 
        """

        date = subprocess.check_output(['date']).decode('utf-8')
        await message.reply(date)

except subprocess.CalledProcessError as e:
    print("Ошибка:", e)