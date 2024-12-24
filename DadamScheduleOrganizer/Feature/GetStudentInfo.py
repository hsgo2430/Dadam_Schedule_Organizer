import pdfplumber

from Model.Student import Student
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

def getStudentDataFromPDF(filePath):
    # PDF 열기
    with pdfplumber.open(filePath) as pdf:
        for page in pdf.pages:
            # 페이지에서 표 추출
            tables = page.extract_tables()  # 테이블만 출력
            studentInfo = tables[0]
            studentTimeTable = tables[1]

            student = createStudent(studentInfo)
            student.setTimetable(arrangeStudentTimeTable(studentTimeTable))

    print(student.name)
    print(student.studentId)
    print(student.major)
    # 결과 출력
    for idx, row in enumerate(student.timeTable):
        print(f"Row {idx}: {row}")


getStudentDataFromPDF("C:/Users/hsgo2/Dadam/DadamTimeTable/(박수진)[전공교육지원센터] 2024학년도 2학기 근로멘토장학생 신청서.pdf")