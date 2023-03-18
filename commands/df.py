# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python


import subprocess
from aiogram import types

async def df_command(message: types.Message):
    """
    Функция использует модуль subprocess для выполнения команды "df -h",
    в терминале и получения информации о диске.
    """

    try:
        df = subprocess.check_output(['df', '-h']).decode('utf-8')
        await message.reply(df)
    except subprocess.CalledProcessError as e:
        error_message = f"Произошла ошибка: {e.returncode} - {e.output.decode('utf-8')}"
        await message.reply(error_message)
