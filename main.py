import sys
import os

from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap

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

        for path in os.listdir(globals.active_folder_path):
            full_path = os.path.join(globals.active_folder_path, path)
            globals.active_files.append(full_path)
            # if os.path.isfile(full_path):


        # for (dirpath, dirnames, filenames) in walk(globals.active_folder_path):
        #     for file in filenames:
        #         globals.active_files.append(abspath(file))
        #
        #     for dir in dirnames:
        #         globals.active_sub_dirs.append(abspath(dir))


    def next_file(self):

        print(globals.active_files)
        print(globals.active_files_index)

        if globals.active_files_index >= len(globals.active_files):
            globals.active_files_index = 0

        new_pixmap = QPixmap(globals.active_files[globals.active_files_index])
        self.active_image_pixmap.setPixmap(new_pixmap)

        globals.active_files_index = globals.active_files_index + 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec()