import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, \
    QTabWidget, QFormLayout, QLineEdit, QRadioButton, QCheckBox, QPushButton


# 自定义选项卡QTabWidget类
class myTabWidget(QTabWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置选项卡的位置、大小、标题和标签位置（上： North）
        self.setGeometry(300, 300, 360, 160)
        self.setWindowTitle('QTabWidget测试')
        self.setTabPosition(QTabWidget.TabPosition.North)
        # 创建用于显示控件的2个QWidget窗口对象tabW1、tabW2
        self.tabW1 = QWidget()
        self.tabW2 = QWidget()
        # tabW1、tabW2窗口分别加入选项卡1和选项卡2
        self.addTab(self.tabW1, '选项卡1')
        self.addTab(self.tabW2, '选项卡2')
        self.tabW1_UI()
        self.tabW2_UI()

    # 定义窗口对象tabW1界面控件
    def tabW1_UI(self):
        fLayout = QFormLayout()
        self.xm = QLineEdit()
        self.xb1 = QRadioButton('男')
        self.xb2 = QRadioButton('女')
        self.xb1.setChecked(True)
        self.csny = QLineEdit()
        btn = QPushButton("确定")
        btn.clicked.connect(self.clickedFunc)

        hLay = QHBoxLayout()
        hLay.addWidget(self.xb1)
        hLay.addWidget(self.xb2)
        fLayout.addRow('姓名: ', self.xm)
        fLayout.addRow('性别: ', hLay)
        fLayout.addRow('出生年月: ', self.csny)
        fLayout.addRow(' ', btn)
        self.setTabText(0, '基本信息')  # 修改第1个选项卡标题
        self.tabW1.setLayout(fLayout)


    # 定义窗口对象tabW2界面控件
    def tabW2_UI(self):
        hLay = QHBoxLayout()
        self.cb1 = QCheckBox('C++')
        self.cb2 = QCheckBox('Java')
        self.cb3 = QCheckBox('C#')
        self.cb1.setChecked(True)
        hLay.addWidget(self.cb1)
        hLay.addWidget(self.cb2)
        hLay.addWidget(self.cb3)
        self.setTabText(1, '编程语言')  # 修改第2个选项卡标题
        self.tabW2.setLayout(hLay)


    # 命令按钮单击槽函数，
    def clickedFunc(self):
        # ---检查第1个选项卡中的控件
        print(self.xm.text())
        print(self.csny.text())
        if self.xb1.isChecked():
            print(self.xb1.text())
        else:
            print(self.xb2.text())
        # ---检查第2个选项卡中的控件
        if self.cb1.isChecked():
            print(self.cb1.text())
        if self.cb2.isChecked():
            print(self.cb2.text())
        if self.cb3.isChecked():
            print(self.cb3.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = myTabWidget()  # 创建选项卡对象
    w.show()
    sys.exit(app.exec())
