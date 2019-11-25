# Проверяльщик статусов заданий на https://dvmn.org/

## Использованные модули:
* Python telegram bot: https://github.com/python-telegram-bot/python-telegram-bot


## Системные требования:
python3.5+

## Установка:
```bash
$ pip install -r requirements.txt

```

### Пропишите свои секретные ключи
Переименуйте файл dotenv_example в .env и заполните своими данными:
* DEVMAN_TOKEN - токен, выданный вам девманом
* TG_BOT_API_KEY - ключ полученный от BotFather

### Пропишите ваш chat_id в файле config.py (необязательно)

## Запуск приложения:

```bash
$ python main.py
```
Если вы не прописали chat_id в файле config.py или хотите использовать другой чат, передайте его в командной строке:

```bash
$ python main.py 123456789
```

## Цели проекта:
Код написан в образовательных целях, в рамках онлайн-курса dvmn.org


