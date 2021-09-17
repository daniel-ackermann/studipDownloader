import json


class Settings:
    settingsFile = ""
    fileContent = {}

    def __init__(self, filename) -> None:
        self.settingsFile = filename
        try:
            file = open(self.settingsFile)
            self.fileContent = json.load(file)
            file.close()
        except Exception:
            self.fileContent = {
                "auth": {
                    "username": "",
                    "password": ""
                },
                "mainUrl": "https://studip.uni-goettingen.de",
                "courses": {}
            }
            self.saveSettings()


    def getMainUrl(self):
        return self.mainUrl

    def loadCourses(self):
        return self.fileContent['courses']

    def storeCourses(self, courses):
        self.fileContent['courses'] = courses
        self.saveSettings()

    def saveSettings(self):
        file = open(self.settingsFile, "w")
        json.dump(self.fileContent, file)
        file.close()

    def getMainUrl(self):
        return self.fileContent['mainUrl']

    def setMainUrl(self, url):
        self.fileContent['mainUrl'] = url
        self.saveSettings()

    def setUserid(self, id):
        self.fileContent['userid'] = id
        self.saveSettings()

    def getUserid(self):
        if self.hasUserid():
            return self.fileContent['userid']

    def hasUserid(self):
        if 'userid' in self.fileContent:
            return True
        return False

    def hasAuth(self):
        if 'auth' in self.fileContent and 'password' in self.fileContent['auth'] and 'username' in self.fileContent['auth']:
            if self.fileContent['auth']['username'] != "" and self.fileContent['auth']['password'] != "":
                return True
        return False

    def getAuth(self):
        return self.fileContent['auth']

    def getPassword(self):
        return self.fileContent['auth']['password']

    def getUsername(self):
        return self.fileContent['auth']['username']

    def setUsername(self, newName):
        self.fileContent['auth']['username'] = newName
        self.saveSettings()

    def setPassword(self, newPassword):
        self.fileContent['auth']['password'] = newPassword
        self.saveSettings()
