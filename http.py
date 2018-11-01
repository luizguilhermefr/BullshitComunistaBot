import requests


class Http:
    @staticmethod
    def get(url):
        headers = {
            'Accept': 'application/json'
        }
        res = requests.get(url, headers=headers)
        return res.json()

    @staticmethod
    def post(url, data):
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        res = requests.post(url, headers=headers, data=data)
        return res.json()
