import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

from UI.ProgramUI import Ui_MainWindow

if __name__ == "__main__":
    # 애플리케이션 초기화
    app = QApplication(sys.argv)

    # 메인 윈도우 생성 및 설정
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # 메인 윈도우 표시
    MainWindow.show()

    # 이벤트 루프 실행
    sys.exit(app.exec_())