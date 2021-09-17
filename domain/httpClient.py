import requests

class HttpClient:
    def __init__(self, auth) -> None:
        self.auth = auth
    def requestAuth(self, url):
        try:
            return requests.get(url, auth=(self.auth['username'], self.auth['password'])).json()
        except Exception as err:
            print("Zugriff auf Web-Resource fehlgeschlagen: " + url)
            return err