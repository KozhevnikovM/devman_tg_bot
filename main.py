import requests
from config import DEVMAN_TOKEN
from time import sleep, time
from bot import send_telegram_message
import argparse
from config import TELEGRAM_CHAT_ID


def get_checked_works(timestamp=time()):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {DEVMAN_TOKEN}'
    }
    params = {
        'timestamp': timestamp
    }
    response = requests.get(url, headers=headers, params=params)
    if not response.ok:
        requests.Response.raise_for_status(response)
    return response.json()


def check_permanently():
    timestamp = 0
    while True:
        try:
            response = get_checked_works(timestamp)
            timestamp = response['last_attempt_timestamp'] if 'last_attempt_timestamp' in response \
                else response['timestamp_to_request']
            yield response
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            continue


def prepare_message(attempts):
    attempt = attempts[0]
    positive_message = 'Преподавателю все понравилось, можно приступать к следующему уроку'
    negative_message = 'К сожалению, в работе нашлись ошибки'
    status = negative_message if attempt['is_negative'] else positive_message
    return f'У вас проверили работу: \"{attempt["lesson_title"]}\" \n\n ' \
           f'{status} \n\n ' \
           f'Подробнее по ссылке: https://dvmn.org/{attempt["lesson_url"]}'


def parse_chat_id():
    parser = argparse.ArgumentParser()
    parser.add_argument('chat_id', type=int, nargs='?')
    args = parser.parse_args()
    return args.chat_id


if __name__ == '__main__':
    chat_id = parse_chat_id() or TELEGRAM_CHAT_ID

    for checking in check_permanently():
        if checking['status'] == 'found':
            message = prepare_message(checking['new_attempts'])
            send_telegram_message(chat_id, message)
