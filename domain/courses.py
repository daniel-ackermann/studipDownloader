from domain.course import Course
from domain.httpClient import HttpClient

class Courses:
    courses = {}
    changesCallback = ""
    
    def __init__(self, settings) -> None:
        self.settings = settings
        self.httpClient = HttpClient(settings.getAuth())
        data = settings.loadCourses()
        for course in data:
            self.courses[course] = Course(data[course], self.settings)
            self.courses[course].onRemove = self.removeCourse
    
    def addCourse(self, course):
        print("add course: " + course['title'])
        self.courses[course['course_id']] = Course({
            "download": True,
            "path": course['title'],
            "title": course['title'],
            "id": course['course_id']
        }, self.settings)
        self.courses[course['course_id']].onRemove = self.removeCourse
        self.settings.storeCourses(self.getJSON())
        index = course['course_id']
        self.changesCallback(self.courses[index])
    
    def removeCourse(self, index):
        print("remove course: " + index)
        del self.courses[index]
        self.settings.storeCourses(self.getJSON())

    def getAvailabe(self):
        res = self.httpClient.requestAuth("https://studip.uni-goettingen.de/api.php/user/" + self.settings.getUserid() + "/courses?limit=100")
        return res['collection']
    
    def getCourses(self):
        return self.courses
    
    def downloadAll():
        pass

    def onChange(self, callback):
        self.changesCallback = callback

    def getJSON(self):
        res = {}
        for c in self.courses:
            res[c] = self.courses[c].getJson()
        return res
    
    def print(self):
        if not self.courses:
            print("Noch keine Kurse")
        for course in self.courses:
            print(self.courses[course].getTitle())
