import pdfplumber

from Model.Student import Student, Worker


def createStudent(studentInfo):
    studentName = studentInfo[0][1]
    studentId = studentInfo[1][1]
    studentMajor = studentInfo[1][3]

    return Student(studentName, studentId, studentMajor)


def arrangeStudentTimeTable(studentTimeTable):
    studentWeekTimeTable = []

    studentTimeTableRearranged = list(map(list, zip(*studentTimeTable)))
    studentTimeTableRearranged.pop(0)

    for timeTableFactor in studentTimeTableRearranged:
        timeTableFactor.pop(0)
        studentWeekTimeTable.append(timeTableFactor)

    return studentWeekTimeTable

def getNewStudentDataFromPDF(filePath):
    # PDF 열기
    with pdfplumber.open(filePath) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()  # 테이블만 출력
            studentInfo = tables[0]
            studentTimeTable = tables[1]

            student = createStudent(studentInfo)
            student.setTimetable(arrangeStudentTimeTable(studentTimeTable))
            student.setWorker(Worker.NEW)

    return student


def getExistStudentDataFromPDF(filePath):
    # PDF 열기
    with pdfplumber.open(filePath) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()  # 테이블만 출력
            studentInfo = tables[0]
            studentTimeTable = tables[1]

            student = createStudent(studentInfo)
            student.setTimetable(arrangeStudentTimeTable(studentTimeTable))
            student.setWorker(Worker.EXISTING)

    return student
