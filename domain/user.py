from domain.httpClient import HttpClient


class User:
    user = {}
    def __init__(self, settings) -> None:
        self.httpClient = HttpClient(settings.getAuth())
        self.user = self.httpClient.requestAuth("https://studip.uni-goettingen.de/api.php/user")
    def getId(self):
        return self.user['user_id']