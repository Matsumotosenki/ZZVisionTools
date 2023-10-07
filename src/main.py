"""
Author:Qychui
DATE:2023/9/12 14:03
File:main.py
"""
import sys

from PyQt6.QtWidgets import QApplication
from ui.main_windows import MainWindows

def main():
    app = QApplication(sys.argv)
    ex = MainWindows()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()