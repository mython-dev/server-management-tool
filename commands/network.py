# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python


import asyncio
import subprocess
from aiogram import types

async def command_network(message: types.Message):

    try:
        # Запуск команду 'ifconfig' с помощью asyncio.create_subprocess_shell() и сохранит ее вывод в переменную с именем ifconfig.
        result = await asyncio.create_subprocess_shell('ifconfig', stdout=subprocess.PIPE)
        ifconfig = await result.stdout.read()

        # Проверка, длиннее ли выходные данные 4096 байт. Если это так,  записать его в файл и  отправить этот файл как документ.
        if len(ifconfig) > 4096:
            with open('ifconfig.txt', 'w') as file:
                file.write(ifconfig.decode())

            with open('ifconfig.txt', 'rb') as file:
                # Отправить файл.
                await message.reply('Отправляю пожалуйста подаждите...')
                await message.reply_document(file, caption='Ловите...')

        # Если выходные данные короче или равны 4096 байтам, отправить их как обычное сообщение.
        else:
            await message.reply(ifconfig.decode())

    #  Перехват любые исключения, которые могут возникнуть во время выполнения, и  отправить пользователю сообщение об ошибке.
    except Exception as e:
        error_message = f"Произошла ошибка: {str(e)}"
        await message.reply(error_message)
