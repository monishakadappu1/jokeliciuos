import requests
import exceptions as e

class Joke:
    def __init__(self):
        self.url = 'https://api.jokes.one/jod?category=knock-knock'
        self.api_token = ""
        self.headers = {'content-type': 'application/json',
                   'X-JokesOne-Api-Secret': format(self.api_token)}
        self.resp = ""

    def getjoke(self):
        try:
            self.resp = requests.get(self.url, headers=self.headers)
            jokes = self.resp.json()
            return jokes['contents']['jokes'][0]['joke']['text']
        except:
            raise e.ApiError("GET /jokes/ {}".format(self.resp.status_code))


