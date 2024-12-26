from openpyxl import load_workbook

def getExcelFile(filePath):
    print()


def findLastRowIndex(work_space, col, row):
    last_row = row
    while work_space[f"{chr(last_row)}{col}"].value is not None:
        last_row += 1

    return last_row

def findLastColIndex(work_space, col, row):
    last_col = col
    while work_space[f"{chr(row)}{last_col}"].value is not None:
        last_col += 1

    return last_col