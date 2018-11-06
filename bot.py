from activation import activation_words
from bullshit import make_bullshit
from http_client import HttpClient


class Bot:
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.updates = None

    def update(self, last_update_id):
        url = self.url + 'getUpdates?timeout=100'
        if last_update_id:
            url += '&offset={}'.format(last_update_id)
        self.updates = HttpClient.get(url)

    def get_last_update_id(self):
        if self.updates is None:
            return None
        last_updates = []
        for update in self.updates['result']:
            last_updates.append(int(update['update_id']))
        return max(last_updates)

    def has_messages(self):
        return self.updates is not None and len(self.updates['result']) > 0

    @staticmethod
    def is_group_message(message):
        return message['chat']['type'] == "group"

    @staticmethod
    def should_reply(message):
        if 'text' in message:
            text = message['text']
            for token in str.lower(text).split(' '):
                if token in activation_words:
                    return True
        return False

    def handle(self):
        for update in self.updates['result']:
            message = update['message']
            if self.should_reply(message):
                chat_id = message['chat']['id']
                self.send(chat_id)
                break

    def send(self, chat_id):
        print('Sending message...')
        text = make_bullshit()
        url = self.url + 'sendMessage?text={}&chat_id={}'.format(text, chat_id)
        res = HttpClient.get(url)
        print(res)
