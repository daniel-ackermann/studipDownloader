#!/usr/bin/env python3.8


from domain.settings import Settings
from domain.course import Course
from domain.user import User
from domain.courses import Courses
from gui.application import Application

settings = Settings("./settings.json")

if not settings.hasAuth():
    print("Credentials missing! Edit settings.json. Your username has a format like 'name.surname'.")
    exit()

if not settings.hasUserid():
    user = User(settings)
    settings.setUserid(user.getId())



courses = Courses(settings)

# Hier die Kurse die ein Nutzer potenziell runterladen könnte zu übergeben ist unschön
# Wie mache ich es besser? Courses weg lassen? Wie könnte ich dann die Funktionen von Curses ersetzen?
app = Application(courses.getAvailabe(), settings)

courses.onChange(app.displayCourse)

app.onChange(courses.addCourse)

app.listCourses(courses.getCourses())

app.mainloop()