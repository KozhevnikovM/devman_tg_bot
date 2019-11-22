import requests
from config import DEVMAN_TOKEN
from time import sleep, time
from bot import tg_send_message


def get_checked_list(timestamp=time()):
    url = 'https://dvmn.org/api/long_polling/'
    headers = {
        'Authorization': f'Token {DEVMAN_TOKEN}'
    }
    params = {
        'timestamp': timestamp
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()


def continuous_checking():
    timestamp = 0
    while True:
        try:
            response = get_checked_list(timestamp)
            timestamp = response['last_attempt_timestamp'] if 'last_attempt_timestamp' in response \
                else response['timestamp_to_request']
            yield response
        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectionError):
            yield


def prepare_message(checking):
    if checking['status'] == 'found':
        attempt = checking["new_attempts"][0]
        positive_message = 'Преподавателю все понравилось, можно приступать к следующему уроку'
        negative_message = 'К сожалению, в работе нашлись ошибки'
        status = negative_message if attempt['is_negative'] else positive_message
        return f'У вас проверили работу: \"{attempt["lesson_title"]}\" \n\n ' \
               f'{status} \n\n ' \
               f'Подробнее по ссылке: https://dvmn.org/{attempt["lesson_url"]}'


if __name__ == '__main__':
    for checking in continuous_checking():
        if checking['status'] == 'found':
            message = prepare_message(checking)
            tg_send_message(message)
