from activation import activation_words
from bullshit import make_bullshit
from http import Http


class Bot:
    def __init__(self, url, token):
        self.url = url
        self.token = token
        self.updates = None

    def update(self, last_update_id):
        url = self.url + 'getUpdates?timeout=100'
        if last_update_id:
            url += '&offset={}'.format(last_update_id)
        self.updates = Http.get(url)

    def get_last_update_id(self):
        if self.updates is None:
            return None
        last_updates = []
        for update in self.updates['result']:
            last_updates.append(int(update['update_id']))
        return max(last_updates)

    def has_messages(self):
        return self.updates is not None and len(self.updates['result']) > 0

    def handle(self):
        for update in self.updates['result']:
            text = update['message']['text']
            chat_id = update['message']['chat']['id']
            for token in str.lower(text).split(' '):
                if token in activation_words:
                    self.send(chat_id)
                    break

    def send(self, chat_id):
        data = {
            'text': make_bullshit(),
            'chat_id': chat_id
        }
        url = self.url + 'sendMessage'
        Http.post(url, data)
