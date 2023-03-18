# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python

from aiogram import types 
import subprocess

async def shutdown_command(message: types.Message):

    """
    имя функции - shutdown_command. 
    Она вызывается, когда пользователь отправляет команду "/shutdown" боту. 
    Функция отправляет ответное сообщение с текстом "Выключение сервера…" и вызывает команду sudo shutdown now, 
    чтобы выключить сервер.
    """
    
    await message.reply('Выключение сервера…')
    try:
        # Выполняем команду для выключения сервера с помощью утилиты sudo и shutdown
        subprocess.check_call(['sudo', 'shutdown', 'now'])
    except subprocess.CalledProcessError as e:
        # Если произошла ошибка при выполнении команды, отправляем сообщение об ошибке в Telegram
        await message.reply(f'Произошла ошибка: {e}')


        