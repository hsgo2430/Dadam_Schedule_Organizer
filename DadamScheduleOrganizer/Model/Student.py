from enum import Enum


class Student:
    def __init__(self, name, studentId, major):
        self.name = name
        self.studentId = studentId
        self.major = major
        self.timeTable = None
        self.worker = None

    def setTimetable(self, timeTable):
        self.timeTable = timeTable

    def setWorker(self, worker):
        self.worker = worker

    def printStudentInfo(self):
        print(self.name)
        print(self.studentId)
        print(self.major)
        # 결과 출력
        for idx, row in enumerate(self.timeTable):
            print(f"Row {idx}: {row}")


class Worker(Enum):
    EXISTING = 1
    NEW = 2