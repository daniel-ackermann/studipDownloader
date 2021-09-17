import tkinter as tk
from tkinter import ttk

# local imports
from domain.settings import Settings
from gui.settingsDialog import SettingsDialog
from gui.scrollableFrame import ScrollableFrame

root = tk.Tk()
root.geometry("800x400")
root.grid_columnconfigure(0, weight=4)
root.grid_columnconfigure(1, weight=4)


class Application(tk.Frame):
    def __init__(self, available, settings):
        super().__init__(root)
        self.master = root
        self.master.title("Studip-Client")
        self.courses = {}
        self.availableCourses = available
        self.index = 1
        self.settings = settings

        header = self.printHeader(self.master)
        # header.place(x=0, y=0, anchor="nw", width=375, height=115)
        header.grid(column=0, row=0)

    def remove(self, course):
        index = course.id
        self.courses[index]['label'].destroy()
        self.courses[index]['downloadPath'].destroy()
        self.courses[index]['startDownloadButton'].destroy()
        self.courses[index]['stopDownloadButton'].destroy()
        self.courses[index]['removeButton'].destroy()
        course.removeCourse(index)

    def printHeader(self, container):
        nb_of_columns = 5  # to be replaced by the relevant number
        settingsDialog = SettingsDialog(self.master, self.settings)
        titleframe = tk.Frame(container, bg="white")

        titleframe.grid_columnconfigure(0, weight=4)
        titleframe.grid_columnconfigure(1, weight=4)

        titleframe.grid(row=0, column=0, columnspan=nb_of_columns, sticky='ew')

        label = ttk.Label(titleframe, text="Studip-Client", background="white")
        openSettings = ttk.Button(
            titleframe, text="Einstellungen", command=settingsDialog.showSettings)
        openCourses = ttk.Button(
            titleframe, text="Kurse", command=self.showAddCourseList)

        label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=20)
        openSettings.grid(column=4, row=0, sticky=tk.E, padx=5, pady=20)
        openCourses.grid(column=3, row=0, sticky=tk.E, padx=5, pady=20)

        return titleframe

    def listCourses(self, courses):
        for index in courses:
            self.displayCourse(courses[index])

    def displayCourse(self, course):
        index = course.id
        self.courses[index] = {}
        
        self.courses[index]['label'] = tk.Label(
            self.master, text=course.getTitle(), anchor="w")
        self.courses[index]['label'].grid(row=self.index, column=0, sticky="w")

        self.courses[index]['downloadPath'] = tk.Entry(self.master)
        self.courses[index]['downloadPath'].insert(0, course.path)
        self.courses[index]['downloadPath'].grid(row=self.index, column=3, sticky="ew")
        
        self.courses[index]['startDownloadButton'] = tk.Button(
            self.master, text="Download", command=course.startDownloadFiles)
        self.courses[index]['startDownloadButton'].grid(row=self.index, column=1)
        
        self.courses[index]['stopDownloadButton'] = tk.Button(
            self.master, text="Stop", command=course.stopDownloadFiles)
        self.courses[index]['stopDownloadButton'].grid(row=self.index, column=2)

        self.courses[index]['removeButton'] = tk.Button(
            self.master, text="Entfernen", command=lambda y=course:  self.remove(y))
        self.courses[index]['removeButton'].grid(row=self.index, column=4)

        self.index += 1

    def onChange(self, callback):
        self.onChangeCallback = callback

    def showAddCourseList(self):
        # Wie kann ich hier schön auf courses.addCourse() zugreifen?
        # Eigene Instanz erzeugen geht nicht -> single source of truth
        # Instanz aus der main.py dem Konstruktor übergeben -> selbes Problem.
        def onCheck(value):
            self.onChangeCallback(value)
        pop = tk.Toplevel(self.master)
        pop.title("Kursauswahl")
        pop.geometry("400x400")
        pop.config(bg="white")
        # Create a Label Text
        label = tk.Label(pop, text="Füge Kurse hinzu:",
                         font=('Aerial', 12), background="white")
        label.pack(pady=20)

        frame = ScrollableFrame(pop)
        for course in self.availableCourses:
            self.availableCourses[course]['checkbox'] = tk.Button(
                frame.scrollable_frame, text=self.availableCourses[course]['title'], command=lambda x=self.availableCourses[course]: onCheck(x))
            self.availableCourses[course]['checkbox'].pack(anchor="w")
        frame.pack()