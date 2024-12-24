class Student:
    def __init__(self, name, studentId, major):
        self.name = name
        self.studentId = studentId
        self.major = major
        self.timeTable = None

    def setTimetable(self, timeTable):
        self.timeTable = timeTable
