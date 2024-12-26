from openpyxl import load_workbook

from Feature.ExcelUtil import findLastRowIndex, findLastColIndex
from Feature.GetStudentInfo import getNewStudentDataFromPDF
from Model.Student import Worker

load_wb = load_workbook("test.xlsx", data_only=True)
student = getNewStudentDataFromPDF("C:/Users/hsgo2/Dadam/DadamTimeTable/(박수진)[전공교육지원센터] 2024학년도 2학기 근로멘토장학생 신청서.pdf")

def putStudentNameMajor(excel, student):
    work_space = excel.active
    if student.worker == Worker.EXISTING:
        last_row = findLastRowIndex(work_space, 4, 67)
        work_space[f"{chr(last_row)}4"] = student.name

    elif student.worker == Worker.NEW:
        last_row = findLastRowIndex(work_space, 6, 67)
        work_space[f"{chr(last_row)}6"] = student.name

    excel.save("test.xlsx")

# def putStudnetTimeSchedule(excel, student):
#     print()



putStudentNameMajor(load_wb, student)