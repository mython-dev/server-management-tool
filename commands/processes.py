# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python

import os
from aiogram import types
import aiogram
from config import BOT_TOKEN

bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.Dispatcher(bot)


async def command_processes(message: types.Message):

    """
    Данная функция выполняет команду 'ps aux' и записывает результат в файл processes.txt.
    Затем открывает этот файл и получает последнюю строку, используя которую может посчитать количество процессов.
    После этого функция отправляет сообщение и документ со списком процессов в чат.
    """
    
    try:
        os.system('ps aux > processes.txt')
    except Exception as e:
        await message.reply(f'Произошла ошибка при записи списка процессов: {str(e)}')
        return

    else:
        
        try:
            with open('processes.txt', 'r') as f:
                lines = f.readlines()
                last_line_number = len(lines) - 1

        except Exception as e:
            await message.reply(f'Произошла ошибка при чтении списка процессов: {str(e)}')
            return
        
        await message.reply('Отправляю список процессов, пожалуйста ждите...')

        try:
            with open('processes.txt', 'rb') as file:
                caption = f'Запущено {last_line_number} процессов.'
                await bot.send_document(message.chat.id, file, caption=caption)
        except Exception as e:
            await message.reply(f"Произошла ошибка при отправте список процессов: {str(e)}")
