import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # UI 파일 불러오기
        ui_file = QFile("main.ui")
        ui_file.open(QFile.ReadOnly)

        loader = QUiLoader()
        self.ui = loader.load(ui_file, self)
        ui_file.close()

        # 버튼 클릭 시 동작 예시 (UI 파일에 'btn_start'라는 이름의 버튼이 있다고 가정)
        # self.ui.btn_start.clicked.connect(self.start_trading)

    def start_trading(self):
        print("트레이딩을 시작합니다!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.ui.show()
    sys.exit(app.exec())