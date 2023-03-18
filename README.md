# Server Management and Monitoring Tool

***
Этот инструмент позволяет вам мониторить и управлять вашим сервером через Telegram.
***

## Установка.

1. Клонировать репозиторий:

```bash
git clone https://github.com/mython-dev/server-management-tool.git
```

2. Перейти в директорию проекта:

```bash
cd server-management-tool
```

3. Установить зависимости.:

```bash
pip install -r requirements.txt
```

4. Открыт файл `config.py` и добавить ваш токен и ваш  Telegram id.

```python
# config.py
BOT_TOKEN = 'yourtelegrambottokenhere'
TLEGRAM_ID = 'yourtelegramidhere'
```

5. Запуск интрумента:

```bash
chmod +x run.sh && chmod +x bot.py
./run.sh
```

## Использование.

После запуска инструмента вы можете взаимодействовать с ним через Telegram. Используйте следующие команды:

- `/start`: приветственное сообщение пользователя.
- `/help`: список доступных команд.
- `/status`: отправляет статус сервера.
- `/date`: показывает время работы сервера.
- `/df`: показывает информацию о дисковом пространстве.
- `/restart`: перезагрузить сервер.
- `/shutdown`: выключить сервер.
- `/install`: установить пакет, используя пакетный менеджер APT.
- `/remove`: удалить пакет.
- `/processes`: получить список процессов.
- `/backup`: сделать резервную копии файла или каталога.
- `/logs`: отправить все логи в /var/log/.
- `/network`: сетевые настройки.

## Скриншоты

<p align = "center">
<img src="https://github.com/mython-dev/server-management-tool/blob/main/screenshots/status.png" width="600" height="600">
</p>

<p align = "center">
<img src="https://github.com/mython-dev/server-management-tool/blob/main/screenshots/df.png" width="600" height="600">
</p>

<p align = "center">
<img src="https://github.com/mython-dev/server-management-tool/blob/main/screenshots/install-remove.png" width="600" height="700">
</p>

<p align = "center">
<img src="https://github.com/mython-dev/server-management-tool/blob/main/screenshots/processes.png" width="600" height="700">
</p>


###  Find Me on 🌐:

- [![Github](https://img.shields.io/badge/Github-mython_dev-green?style=for-the-badge&logo=github)](https://github.com/mython-dev)

- [![Gmail](https://img.shields.io/badge/Gmail-miton0030-green?style=for-the-badge&logo=gmail)](mailto:miton0030@gmail.com)

- [![Instagram](https://img.shields.io/badge/mython_dev--green?style=for-the-badge&logo=instagram)](https://instagram.com/mython_dev)
- [![Instagram](https://img.shields.io/badge/thehackerworld_--green?style=for-the-badge&logo=instagram)](https://instagram.com/thehackerworld_)
