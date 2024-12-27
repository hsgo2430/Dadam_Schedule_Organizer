from openpyxl.reader.excel import load_workbook

from Feature.GetStudentInfo import getExistStudentDataFromPDF, getNewStudentDataFromPDF
from Feature.PutStudentInfo import putStudentNameMajor, putStudnetTimeSchedule


def make_time_table(excel_file_path, student_file_path, is_new_worker):
    if is_new_worker:
        student = getNewStudentDataFromPDF(student_file_path)
    else:
        student = getExistStudentDataFromPDF(student_file_path)

    putStudentNameMajor(excel_file_path, student)
    putStudnetTimeSchedule(excel_file_path, student)
