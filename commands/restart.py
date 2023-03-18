# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python
from aiogram import types
import subprocess
import asyncio


async def restart_command(message: types.Message):
    """
    Функция restart_command 
    выполняет перезагрузку сервера через 3 секунды после получения команды "/restart" от пользователя.
    """
    await message.reply('Перезагрузка сервера... Через 3 секунды.')
    await asyncio.sleep(3)
    
    try:
        subprocess.check_call(['sudo', 'reboot'])
    except subprocess.CalledProcessError as e:
        await message.reply(f'Произошла ошибка: {e}')
