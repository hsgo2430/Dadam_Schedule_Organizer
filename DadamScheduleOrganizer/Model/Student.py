from enum import Enum


class Student:
    def __init__(self, name, studentId, major):
        self.name = name
        self.studentId = studentId
        self.major = major
        self.timeTables = list()
        self.worker = None

    def setTimetable(self, timeTable):
        self.timeTables.append(timeTable)

    def setWorker(self, worker):
        self.worker = worker

    def printStudentInfo(self):
        print(self.name)
        print(self.studentId)
        print(self.major)
        # 결과 출력
        for timeTable in self.timeTables:
            for idx, row in enumerate(timeTable):
                print(f"Row {idx}: {row}")
            print("==========================================")

        print(len(self.timeTables))


class Worker(Enum):
    EXISTING = 1
    NEW = 2