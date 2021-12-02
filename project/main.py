import sys
from PySide6.QtGui import QPixmap 
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication,  QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('My first application')
        self.resize(800, 600)

        mainwindow = QHBoxLayout(self)

        left_menu = QLabel()
        left_menu_layout = QVBoxLayout(left_menu)
        left_menu_layout.addWidget(QPushButton('색공간'))
        left_menu_layout.addWidget(QPushButton('임계 처리'))
        left_menu_layout.addWidget(QPushButton('산술 연산'))
        left_menu_layout.addWidget(QPushButton('기하하적 변환'))
        left_menu_layout.addWidget(QPushButton('영상 필터'))
        left_menu_layout.addWidget(QPushButton('경계 검출'))
        left_menu_layout.addWidget(QPushButton('영상 분할'))
        left_menu_layout.addWidget(QPushButton('가우시안 필터링'))
        left_menu_layout.setAlignment(Qt.AlignTop)
        #이미지 넣기

        right_content =QLabel()
        image = QPixmap('./cat-01.jpg')
        right_content.setPixmap(image)

        mainwindow.addWidget(left_menu)
        mainwindow.addWidget(right_content)


        mainwindow.addWidget(left_menu)
        # mainwindow.addWidget()

        self.setLayout(mainwindow)
        self.setGeometry(500, 500, 1280, 720)
        self.show()

if __name__ == '__main__':
    app = QApplication()
    ex = MyApp()
    sys.exit(app.exec())