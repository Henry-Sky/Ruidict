# 系统界面包
import sys
from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication
# 功能包
import youdao

apis = {
    "有道":youdao
}

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("Ruidict.ui",self)
        self.UIinit()

    def UIinit(self):
        self.ui.word_txt.setPlaceholderText("输入待翻译单词")
        self.ui.trans_btn.clicked.connect(self.translate)
        self.ui.exp_lab.setWordWrap(True)
        self.ui.dict_box.addItems(apis.keys())


    def translate(self):
        word = self.ui.word_txt.toPlainText()
        print("按钮点击事件触发")
        print("输入单词:{}".format(word))
        dict = apis[self.ui.dict_box.currentText()]
        explains = dict.get_explains(word)
        print("翻译结果:{}".format(explains))
        self.ui.exp_lab.setText(str(explains))

def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()