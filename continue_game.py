from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_continue_game(object):
    x_before = ""
    x_after = ""
    x_score_before = 0
    x_score_after = 0

    zero_before = ""
    zero_after = ""
    x_zero_before = 0
    x_zero_after = 0

    def start_cont(self):
        a = self.radioButton_1.isChecked()
        if a:
            self.x_after = self.x_before
            self.zero_after = self.zero_before
        else:
            self.x_after = self.zero_before
            self.zero_after = self.x_before

        self.window1 = QtWidgets.QMainWindow()
        self.main_d = Ui_Dialog()
        self.main_d.player_1_name.setText(self.x_after)
        self.main_d.player_1_name_2.setText(self.zero_after)
        continue_game.destroy()

    def setupUi(self, continue_game):
        continue_game.setObjectName("continue_game")
        continue_game.setFixedSize(301, 237)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        continue_game.setWindowIcon(icon)
        continue_game.setStyleSheet("background-color: rgb(152, 152, 114);")
        self.radioButton_1 = QtWidgets.QRadioButton(continue_game)
        self.radioButton_1.setGeometry(QtCore.QRect(60, 60, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(continue_game)
        self.radioButton_2.setGeometry(QtCore.QRect(60, 110, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.player_1_name_2 = QtWidgets.QLabel(continue_game)
        self.player_1_name_2.setGeometry(QtCore.QRect(30, 10, 31, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.player_1_name_2.setFont(font)
        self.player_1_name_2.setStyleSheet("color: rgb(255, 255, 0);")
        self.player_1_name_2.setObjectName("player_1_name_2")
        self.start_button = QtWidgets.QPushButton(continue_game)
        self.start_button.setGeometry(QtCore.QRect(170, 160, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start_button.setFont(font)
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.start_button.setObjectName("start_button")

        self.start_button.clicked.connect(self.start_cont)
        self.retranslateUi(continue_game)
        QtCore.QMetaObject.connectSlotsByName(continue_game)

    def retranslateUi(self, continue_game):
        _translate = QtCore.QCoreApplication.translate
        continue_game.setWindowTitle(_translate("continue_game", "Continue game"))
        self.radioButton_1.setText(_translate("continue_game", self.x_before))
        self.radioButton_2.setText(_translate("continue_game", self.zero_before))
        self.player_1_name_2.setText(_translate("continue_game", "X :"))
        self.start_button.setText(_translate("continue_game", "Start"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    continue_game = QtWidgets.QDialog()
    ui = Ui_continue_game()
    ui.setupUi(continue_game)
    continue_game.show()
    #sys.exit(app.exec_())
