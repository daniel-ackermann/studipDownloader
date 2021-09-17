import requests
import threading
import os
from domain.httpClient import HttpClient

class DownloadThread(threading.Thread):
    queue = []
    isRunning = False
    def __init__(self, settings):
        threading.Thread.__init__(self)
        self.settings = settings
        self.httpClient = HttpClient(settings.getAuth())
    def add(self, folder, path):
        print("worker: add elem")
        self.queue.append({
            "folder": folder,
            "path": path
        })
    def quit(self):
        self.queue = []
    def run(self):
        if self.isRunning:
            return
        print("worker: start")
        self.isRunning = True
        while self.queue:
            current = self.queue.pop(0)
            self.downloadFolder(current['folder'], current['path'])
        print("worker: done")
        self.isRunning = False
    def downloadFolder(self, folder, path):
        if not os.path.exists(path):
            os.mkdir(path)
        if folder['file_refs']:
            for file in folder['file_refs']:
                if not os.path.exists(path + "/" + file['name']):
                    print("download: " + path + "/" + file['name'])
                    self.downloadFile(self.settings.getMainUrl() + "/api.php/file/"+ file['file_id'] +"/download", path + "/" + file['name'])
        if folder['subfolders']:
            for subfolder in folder['subfolders']:
                try:
                    subfolder = self.httpClient.requestAuth(self.settings.getMainUrl() + "/api.php/folder/" + subfolder['id'])
                    self.add(subfolder, path + "/" + subfolder['name'])
                except Exception as err:
                    print(err)
                    return err
    def downloadFile(self, url, path):
        r = requests.get(url, stream=True)
        with open(path, 'wb') as f:
            f.write(r.content)