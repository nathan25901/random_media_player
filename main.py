import sys
import os
import PyQt6.QtCore
from win32api import GetSystemMetrics

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from random import shuffle

import globals


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        subwindow = SubWindow()

        # Set the central widget of the Window.
        self.setCentralWidget(subwindow)


class SubWindow(QScrollArea):
    def __init__(self):
        super(SubWindow, self).__init__()
        layout = QVBoxLayout()
        primary_layout = self.primary_layout()
        layout.addLayout(primary_layout)
        self.setLayout(layout)

    def primary_layout(self):
        layout = QGridLayout()

        choose_new_directory_button = QPushButton("Choose New Directory")
        choose_new_directory_button.clicked.connect(self.change_directory)
        next_button = QPushButton("Next")
        next_button.clicked.connect(self.next_file)
        previous_button = QPushButton("Previous")

        pixmap = QPixmap('C:\\Users\\Nathan\\Desktop\\imgs\\Potatoe.jpg')
        self.active_image_pixmap = QLabel()
        self.active_image_pixmap.setPixmap(pixmap)

        layout.addWidget(self.active_image_pixmap, 0, 0, 1, 3)

        layout.addWidget(choose_new_directory_button, 1, 0)
        layout.addWidget(previous_button, 1, 1)
        layout.addWidget(next_button, 1, 2)

        return layout

    def change_directory(self):
        dlg = QFileDialog()
        globals.active_folder_path = dlg.getExistingDirectory(self)

        temp_active_files = []

        for path in os.listdir(globals.active_folder_path):
            full_path = os.path.join(globals.active_folder_path, path)
            temp_active_files.append(full_path)

        shuffle(temp_active_files)
        print(temp_active_files)
        globals.active_files = temp_active_files

    def next_file(self):
        if globals.active_files_index >= len(globals.active_files):
            globals.active_files_index = 0

        new_pixmap = QPixmap()

        while new_pixmap.isNull():
            new_pixmap = QPixmap(globals.active_files[globals.active_files_index])
            globals.active_files_index = globals.active_files_index + 1

        width, height = self.get_monitor_resolution()
        new_pixmap = new_pixmap.scaled(height-500, width-50, PyQt6.QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.active_image_pixmap.setPixmap(new_pixmap)

    def get_monitor_resolution(self):
        return int(GetSystemMetrics(0)), int(GetSystemMetrics(1))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()