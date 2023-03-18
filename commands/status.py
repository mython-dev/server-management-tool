import subprocess  # для запуска внешних процессов
import speedtest # для тестирования скорости интернета
import psutil # для работы с процессами и системными ресурсами
import asyncio  # для асинхронных операций

from aiogram import types
import aiogram
from config import BOT_TOKEN, TELEGRAM_ID

bot = aiogram.Bot(token=BOT_TOKEN)
dp = aiogram.Dispatcher(bot)


async def send_status():
    # Получаем текущую дату и время
    date = subprocess.check_output(['date']).decode('utf-8')
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
    # Отправляем сообщение с текущим статусом сервера в Telegram
    await bot.send_message(chat_id=TELEGRAM_ID, text=f"🖥️ Статус сервера:\n\n⏰ Дата: {date}💻 Использование CPU: {cpu_usage}% / 100.0%\n🧠 Использование RAM: {ram_usage}% / 100.0%\n💽 Использование диска: {disk_usage}% / 100.0%\n🌐 Скорость загрузки: {download_speed:.2f} Мбит/с Скорость отдачи: {upload_speed:.2f} Мбит/с\n〽️ Пинг: {ping:.2f} мс")

# Создаем функцию для запуска отправки статуса сервера по расписанию
async def scheduled(wait_for):
    while True:
        # Ждем указанное время
        await asyncio.sleep(wait_for)
        # Вызываем функцию отправки статуса сервера
        await send_status()
