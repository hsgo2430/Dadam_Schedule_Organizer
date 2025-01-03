from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtWidgets import QWidget, QPushButton, QMenuBar, QMenu, QStatusBar, QFileDialog, QMessageBox, QAction
import os

from PyQt5.uic.properties import QtWidgets

from Feature.MakeTimeTable import make_time_table


class Ui_MainWindow(object):

    def __init__(self):
        self.excel_file_path = None
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(587, 270)

        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.action.triggered.connect(self.set_execl_file_path)
        # 엑셀 파일 경로 설정

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.ExistingWorkerButton = QPushButton(self.centralwidget)
        self.ExistingWorkerButton.setObjectName(u"ExistingWorkerButton")
        self.ExistingWorkerButton.setGeometry(QRect(150, 30, 291, 61))

        self.ExistingWorkerButton.clicked.connect(self.get_exist_worker_pdf_file)
        # 기존 근무자 pdf 가져오기

        self.NewWorkerButton = QPushButton(self.centralwidget)
        self.NewWorkerButton.setObjectName(u"NewWorkerButton")
        self.NewWorkerButton.setGeometry(QRect(150, 130, 291, 61))

        self.NewWorkerButton.clicked.connect(self.get_new_worker_pdf_file)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 587, 22))

        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.action)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action.setText(QCoreApplication.translate("MainWindow", "경로 설정", None))
        self.ExistingWorkerButton.setText(QCoreApplication.translate("MainWindow", "기존 근무자 시간 추가하기", None))
        self.NewWorkerButton.setText(QCoreApplication.translate("MainWindow", "신규 근무자 시간 추가하기", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", "엑셀 파일 선택", None))
    # retranslateUi

    def set_execl_file_path(self):
        try:
            file_path, _ = QFileDialog.getOpenFileName(None, '엑셀 파일 선택', '../data', 'Excel Files (*.xls *.xlsx *.xlsm *.csv)')
            self.excel_file_path = file_path
            QMessageBox.information(None, '정보', f'엑셀 파일 설정이 완료되었습니다: \n{str(file_path)}')

        except Exception as e:
            QMessageBox.critical(None, '오류', f'파일을 불러오는 중 오류가 발생했습니다: {str(e)}')

    # 엑셀 파일 경로 설정
    def get_exist_worker_pdf_file(self):
        if self.excel_file_path is not None:
            try:
                file_paths, _ = QFileDialog.getOpenFileNames(None, '기존 근무 학생 시간표 파일 선택', '../data', 'PDF Files (*.pdf)')

                if not file_paths:
                    QMessageBox.warning(None, '경고', '선택된 파일이 없습니다.')
                    return

                for student_file_path in file_paths:
                    make_time_table(self.excel_file_path, student_file_path, False)

                QMessageBox.information(None, '정보', '엑셀에 데이터가 저장되었습니다.')

            except Exception as e:
                QMessageBox.critical(None, '오류', f'파일을 불러오는 중 오류가 발생했습니다: {str(e)}')
        else:
            QMessageBox.critical(None, '오류', '엑셀 파일 경로부터 설정해주세요')
    # 기존 근무자의 시간표 파일 가져오기

    def get_new_worker_pdf_file(self):
        if self.excel_file_path is not None:
            try:
                file_paths, _ = QFileDialog.getOpenFileNames(None, '신규 근무 학생 시간표 파일 선택', '../data', 'PDF Files (*.pdf)')

                if not file_paths:
                    QMessageBox.warning(None, '경고', '선택된 파일이 없습니다.')
                    return

                for student_file_path in file_paths:
                    make_time_table(self.excel_file_path, student_file_path, True)

                QMessageBox.information(None, '정보', '엑셀에 데이터가 저장되었습니다.')

            except Exception as e:
                QMessageBox.critical(None, '오류', f'파일을 불러오는 중 오류가 발생했습니다: {str(e)}')
        else:
            QMessageBox.critical(None, '오류', '엑셀 파일 경로부터 설정해주세요')
    # 신규 근무자의 시간표 파일 가져오기