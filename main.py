import time
import configparser

from bot import Bot

bot = None
last_update_id = None


def setup():
    global bot
    config = configparser.ConfigParser()
    config.read('config.ini')
    token = config['DEFAULT']['token']
    url = 'https://api.telegram.org/bot{}/'.format(token)
    bot = Bot(url, token)


def loop():
    global last_update_id, bot
    bot.update(last_update_id)
    if bot.has_messages():
        last_update_id = bot.get_last_update_id() + 1
        bot.handle()
    time.sleep(1)


if __name__ == '__main__':
    setup()
    while True:
        loop()
