from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Save_game(object):
    def setupUi(self, Save_game):
        Save_game.setObjectName("Save_game")
        Save_game.resize(425, 161)
        Save_game.setStyleSheet("background-color: rgb(152, 152, 114);")
        self.lineEdit = QtWidgets.QLineEdit(Save_game)
        self.lineEdit.setGeometry(QtCore.QRect(160, 20, 251, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Save_game)
        self.pushButton.setGeometry(QtCore.QRect(250, 90, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Save_game)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Save_game)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Save_game)
        QtCore.QMetaObject.connectSlotsByName(Save_game)

    def retranslateUi(self, Save_game):
        _translate = QtCore.QCoreApplication.translate
        Save_game.setWindowTitle(_translate("Save_game", "Save game"))
        self.pushButton.setText(_translate("Save_game", "Save"))
        self.label.setText(_translate("Save_game", "Name the game"))
        self.label_2.setText(_translate("Save_game", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Save_game = QtWidgets.QDialog()
    ui = Ui_Save_game()
    ui.setupUi(Save_game)
    Save_game.show()
    sys.exit(app.exec_())

