#!/usr/bin/env python3

# Author        : myth-dev
# GitHub        : https://github.com/mython-dev
# Instagram     : @thehackerworld && @mython_dev
# Telegram      : @myth_dev
# Date          : Saturday, March 18, 2023
# Main Language : Python


# Этот инструмент позволяет вам контролировать и управлять вашим сервером через Telegram.

# Импортируем необходимые модули 

# импортируем пользовательские команды
from commands import backup, date, df, install, logs, remove, restart, shutdown, processes, network, status

 # импортируем  токен бота и id пользователя.
from config import TELEGRAM_ID, BOT_TOKEN

import os # для работы с операционной системой
import subprocess # для запуска внешних процессов
import sys # для работы с операционной системой.

try:
    import asyncio # для асинхронных операций
    import psutil # для работы с процессами и системными ресурсами
    import speedtest # для тестирования скорости интернета
    import docker # для работы с контейнерами Docker
    import aiogram # для работы с Telegram API
    from aiogram import Bot, types, executor, Dispatcher # для работы с Telegram API
    from aiogram.types import *
except ImportError:
    print('Пожалуйста запустите: pip3 install requirements.txt')
    sys.exit()


try:
    os.seteuid(0) # Попытка установить эффективный идентификатор пользователя в 0 (root)
except PermissionError: # Если возникает ошибка PermissionError, выводится сообщение о том, что нужно запустить скрипт с правами суперпользователя
    print("Пожалуйста запустите через: sudo bash run.sh\n")
    sys.exit() # происходит выход из программы.

# создаем объект бота
bot = Bot(token=BOT_TOKEN)
# создаем объект диспетчера
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):

    # Эта функция обрабатывает команду /start и отправляет приветственное сообщение пользователю.

    await bot.send_message(chat_id=TELEGRAM_ID, text='Привет! Я бот для управления серверами Ubuntu/Debian. Введите /help, чтобы узнать, что я могу.')


@dp.message_handler(commands=['help'])
async def help_command(message:types.Message):

    # Эта функция обрабатывает команду /help и отправляет список доступных команд пользователю.


    help_text = """Я могу выполнить следующие команды:\n
/status - отправить статус сервера. 📊
/date - показать время работы сервера. ⏳
/df - показать информацию о дисковом пространстве. 💽
/restart - перезагрузить сервер. 😇
/shutdown - выключить сервер. 😴
/install - установит пакет, c помощью пакетного менеджера APT. ✅
/remove - удалить пакет. ❌
/processes - получить список процессов. 🧐
/backup - сделать резервной копии файла или каталога. 📂
/logs - отправить нужные логи в /var/log/. 📝
/network - сетевые настройки. 🌐
"""

    await bot.send_message(chat_id=TELEGRAM_ID, text=help_text)


@dp.message_handler(commands=["date"])
async def date_handler(message: types.Message):
    # Команда "date"
    # вызывает функцию date_command из модуля date для отправки сообщения с текущей датой и временем.
    await date.date_command(message)

@dp.message_handler(commands=["df"])
async def df_handler(message: types.Message):
    # Команда "df"
    # вызывает функцию df_command из модуля df для отправки сообщения с информацией о дисковом пространстве.
    await df.df_command(message)

@dp.message_handler(commands=["restart"])
async def restart_handler(message: types.Message):
    # Команда "restart"
    # вызывает функцию restart_command из модуля restart для перезапуска системы.
    await restart.restart_command(message)

@dp.message_handler(commands=["shutdown"])
async def shutdown_handler(message: types.Message):
    # Команда "shutdown"
    # вызывает функцию shutdown_command из модуля shutdown для выключения системы.
    await shutdown.shutdown_command(message)

@dp.message_handler(commands=["install"])
async def install_handler(message: types.Message):
    # Команда "install"
    # вызывает функцию install_command из модуля install для установки пакета.
    await install.install_command(message)

@dp.message_handler(commands=["remove"])
async def remove_handler(message: types.Message):
    # Команда "remove"
    # вызывает функцию remove_command из модуля remove для удаления пакета.
    await remove.remove_command(message)

@dp.message_handler(commands=["logs"])
async def logs_handler(message: types.Message):
    # Команда "logs"
    # вызывает функцию send_logs из модуля logs для отправки логов системы.
    await logs.send_logs(message)

@dp.message_handler(commands='backup')
async def backup_handler(message: types.Message):
    # Команда "backup"
    # вызывает функцию backup_command из модуля backup для создания резервной копии системы.
    await backup.backup_command(message)


@dp.message_handler(commands=['processes'])
async def send_processes(message: types.Message):
    # Команда "processes"
    # вызывает функцию command_processes из модуля processes для получения списка процессов в системе.
    await processes.command_processes(message)

@dp.message_handler(commands=['network'])
async def network_command_handler(message: types.Message):
    # Команда "network"
    # вызывает функцию command_network из модуля network для получения информации о сетевых интерфейсах.
    await network.command_network(message)


@dp.message_handler(commands=["status"])
async def status_handler(message: types.Message):
    # Отправляем сообщение об ожидании
    await message.reply('Пожалуйста подождите...')
    await status.send_status()    

async def monitoring_server():
    # Получаем процент использования CPU
    cpu_usage = psutil.cpu_percent()
    # Получаем процент использования оперативной памяти
    ram_usage = psutil.virtual_memory().percent
    # Получаем процент использования диска
    disk_usage = psutil.disk_usage('/').percent
    # Создаем объект speedtest для получения скорости интернета
    st = speedtest.Speedtest()
    # Получаем скорость загрузки, отдачи и пинг
    download_speed, upload_speed, ping = st.download() / 1000000, st.upload() / 1000000, st.results.ping

    if cpu_usage > 90:
        await bot.send_message(chat_id=TELEGRAM_ID, text=f'💻 Использование CPU: <b>{cpu_usage}%</b>, Осталось <b>10%</b> !!!', parse_mode=ParseMode.HTML)

    if ram_usage > 90:
        await bot.send_message(chat_id=TELEGRAM_ID, text=f"🧠 Использование RAM: <b>{ram_usage}%</b>, Осталось <b>10%</b> !!!", parse_mode=ParseMode.HTML)
    
    if disk_usage > 90:
        await bot.send_message(chat_id=TELEGRAM_ID, text=f"💽 Использование диска: <b>{disk_usage}%</b>, Осталось <b>10%</b> !!!", parse_mode=ParseMode.HTML)


async def scheduled_monitoring_server(wait_for):
    while True:
        # Ждем указанное время
        await asyncio.sleep(wait_for)
        # Вызываем функцию отправки статуса сервера
        await monitoring_server()

# если файл запускается как основной скрипт
if __name__ == '__main__':
    loop = asyncio.get_event_loop() 
    loop.create_task(status.scheduled(720)) # запускаем задачу status.scheduled каждые 720 минут (12 часов)
    loop.create_task(scheduled_monitoring_server(300))  # запускаем задачу scheduled_monitoring_serverкаждые 5 минут.
    executor.start_polling(dp, skip_updates=True)