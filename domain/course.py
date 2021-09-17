from domain.worker import DownloadThread
from concurrent import futures
from domain.httpClient import HttpClient
thread_pool_executor = futures.ThreadPoolExecutor(max_workers=1)


class Course:
    download = False
    path = ""
    title = ""
    id = ""
    isDownloading = False

    def __init__(self, course, settings) -> None:
        self.httpClient = HttpClient(settings.getAuth())
        self.settings = settings
        self.download = course['download']
        self.path = course['path']
        self.title = course['title']
        self.id = course['id']

    def addCourse():
        pass

    # wie kann eine solche Methode umgesetzt werden ohne einen callback?
    def removeCourse(self, course):
        self.onRemove(course)

    def startDownloadFiles(self):
        if not self.isDownloading:
            print("start downloading: " + self.title + "...")
            self.isDownloading = True
            try:
                self.downloadFolder(self.getMainFolder(), self.path)
            except Exception as err:
                print(err)
                print("error while downloading " + self.title + " ... stopped")

            self.isDownloading = False

    def stopDownloadFiles(self):
        if self.isDownloading:
            print("stop downloading: " + self.title)
            self.isDownloading = False
            self.worker.quit()

    def getMainFolder(self):
        return self.httpClient.requestAuth(self.settings.getMainUrl() + "/api.php/course/" + self.id + "/top_folder")

    def downloadFolder(self, folder, path):
        self.worker = DownloadThread(self.settings)
        self.worker.add(folder, path)
        self.worker.start()

    def getTitle(self):
        return self.title

    def getJson(self):
        return {
            "download": self.download,
            "path": self.path,
            "title": self.getTitle(),
            "id": self.id
        }
