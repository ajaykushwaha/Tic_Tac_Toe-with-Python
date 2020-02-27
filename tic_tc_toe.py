from PyQt5 import QtCore, QtGui, QtWidgets
from continue_game import Ui_continue_game


class Ui_Dialog(object):
    turn = 'X'
    ttt = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    p1_name = "AJAY"
    p2_name = "GOKUL"
    p1_score = 0
    p2_score = 0

    def disable_all(self):
        self.square11.setEnabled(False)
        self.square12.setEnabled(False)
        self.square13.setEnabled(False)
        self.square21.setEnabled(False)
        self.square22.setEnabled(False)
        self.square23.setEnabled(False)
        self.square31.setEnabled(False)
        self.square32.setEnabled(False)
        self.square33.setEnabled(False)

    def reset_all(self):
        self.turn = 'X'
        self.square11.setEnabled(True)
        self.square12.setEnabled(True)
        self.square13.setEnabled(True)
        self.square21.setEnabled(True)
        self.square22.setEnabled(True)
        self.square23.setEnabled(True)
        self.square31.setEnabled(True)
        self.square32.setEnabled(True)
        self.square33.setEnabled(True)
        self.square11.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square12.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square13.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square21.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square22.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square23.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square31.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square32.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square33.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square11.setText("")
        self.square12.setText("")
        self.square13.setText("")
        self.square21.setText("")
        self.square22.setText("")
        self.square23.setText("")
        self.square31.setText("")
        self.square32.setText("")
        self.square33.setText("")
        self.Result.setText("")

    def continue_play(self):
        self.reset_all()
        self.ttt = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
        self.window = QtWidgets.QMainWindow()
        self.cont = Ui_continue_game()
        self.cont.x_before = self.p1_name
        self.cont.zero_before = self.p2_name

        self.cont.setupUi(self.window)
        self.window.show()

    def focusInEvent(self, event):
        print('focusInEvent')

    def is_win(self, symbol):
        self.Result.setText("AJAY WINS!!!")
        self.continue_button.setEnabled(True)
        if symbol == 'X':
            self.p1_score += 1
            self.lcdNumber.setProperty('value', self.p1_score)
        else:
            self.p2_score += 1
            self.lcdNumber_2.setProperty('value', self.p2_score)
        if self.ttt[0][0] == symbol and self.ttt[0][1] == symbol and self.ttt[0][2] == symbol:
            self.square11.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square12.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square13.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.disable_all()

        elif self.ttt[1][0] == symbol and self.ttt[1][1] == symbol and self.ttt[1][2] == symbol:
            self.square21.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square22.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square23.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.disable_all()

        elif self.ttt[2][0] == symbol and self.ttt[2][1] == symbol and self.ttt[2][2] == symbol:
            self.square31.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square32.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square33.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.disable_all()

        elif self.ttt[0][0] == symbol and self.ttt[1][0] == symbol and self.ttt[2][0] == symbol:
            self.square11.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square21.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square31.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.disable_all()

        elif self.ttt[0][1] == symbol and self.ttt[1][1] == symbol and self.ttt[2][1] == symbol:
            self.square12.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square22.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square32.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.disable_all()

        elif self.ttt[0][2] == symbol and self.ttt[1][2] == symbol and self.ttt[2][2] == symbol:
            self.square13.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square23.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square33.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.disable_all()

        elif self.ttt[0][0] == symbol and self.ttt[1][1] == symbol and self.ttt[2][2] == symbol:
            self.square11.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square22.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square33.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.disable_all()

        elif self.ttt[2][0] == symbol and self.ttt[1][1] == symbol and self.ttt[0][2] == symbol:
            self.square31.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square22.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.square13.setStyleSheet("background-color: rgb(0, 255, 0);")
            self.disable_all()
        else:
            self.Result.setText("")
            if symbol == 'X':
                self.p1_score -= 1
                self.lcdNumber.setProperty('value', self.p1_score)
            else:
                self.p2_score -= 1
                self.lcdNumber_2.setProperty('value', self.p2_score)
            self.continue_button.setEnabled(False)

    def square1_1(self):
        self.square11.setText(self.turn)
        self.ttt[0][0] = self.turn
        self.is_win(self.turn)
        self.turn = 'X' if (self.turn == '0') else '0'
        self.square11.setEnabled(False)

    def square1_2(self):
        self.square12.setText(self.turn)
        self.ttt[0][1] = self.turn
        self.is_win(self.turn)
        self.turn = 'X' if (self.turn == '0') else '0'
        self.square12.setEnabled(False)

    def square1_3(self):
        self.square13.setText(self.turn)
        self.ttt[0][2] = self.turn
        self.is_win(self.turn)
        self.turn = 'X' if (self.turn == '0') else '0'
        self.square13.setEnabled(False)

    def square2_1(self):
        self.square21.setText(self.turn)
        self.ttt[1][0] = self.turn
        self.is_win(self.turn)
        self.turn = 'X' if (self.turn == '0') else '0'
        self.square21.setEnabled(False)

    def square2_2(self):
        self.square22.setText(self.turn)
        self.ttt[1][1] = self.turn
        self.is_win(self.turn)
        self.turn = 'X' if (self.turn == '0') else '0'
        self.square22.setEnabled(False)

    def square2_3(self):
        self.square23.setText(self.turn)
        self.ttt[1][2] = self.turn
        self.is_win(self.turn)
        self.turn = 'X' if (self.turn == '0') else '0'
        self.square23.setEnabled(False)

    def square3_1(self):
        self.square31.setText(self.turn)
        self.ttt[2][0] = self.turn
        self.is_win(self.turn)
        self.turn = 'X' if (self.turn == '0') else '0'
        self.square31.setEnabled(False)

    def square3_2(self):
        self.square32.setText(self.turn)
        self.ttt[2][1] = self.turn
        self.is_win(self.turn)
        self.turn = 'X' if (self.turn == '0') else '0'
        self.square32.setEnabled(False)

    def square3_3(self):
        self.square33.setText(self.turn)
        self.ttt[2][2] = self.turn
        self.is_win(self.turn)
        self.turn = 'X' if (self.turn == '0') else '0'
        self.square33.setEnabled(False)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(727, 480)
        Dialog.setToolTip("")
        Dialog.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(152, 152, 114);")
        self.square11 = QtWidgets.QPushButton(Dialog)
        self.square11.setGeometry(QtCore.QRect(100, 140, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square11.setFont(font)
        self.square11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square11.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square11.setObjectName("square11")
        self.square21 = QtWidgets.QPushButton(Dialog)
        self.square21.setGeometry(QtCore.QRect(100, 240, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square21.setFont(font)
        self.square21.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square21.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square21.setText("")
        self.square21.setObjectName("square21")
        self.square13 = QtWidgets.QPushButton(Dialog)
        self.square13.setGeometry(QtCore.QRect(300, 140, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square13.setFont(font)
        self.square13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square13.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square13.setText("")
        self.square13.setObjectName("square13")
        self.square12 = QtWidgets.QPushButton(Dialog)
        self.square12.setGeometry(QtCore.QRect(200, 140, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square12.setFont(font)
        self.square12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square12.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square12.setText("")
        self.square12.setObjectName("square12")
        self.square22 = QtWidgets.QPushButton(Dialog)
        self.square22.setGeometry(QtCore.QRect(200, 240, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square22.setFont(font)
        self.square22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square22.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square22.setObjectName("square22")
        self.square23 = QtWidgets.QPushButton(Dialog)
        self.square23.setGeometry(QtCore.QRect(300, 240, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square23.setFont(font)
        self.square23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square23.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square23.setText("")
        self.square23.setObjectName("square23")
        self.square31 = QtWidgets.QPushButton(Dialog)
        self.square31.setGeometry(QtCore.QRect(100, 340, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square31.setFont(font)
        self.square31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square31.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square31.setText("")
        self.square31.setObjectName("square31")
        self.square32 = QtWidgets.QPushButton(Dialog)
        self.square32.setGeometry(QtCore.QRect(200, 340, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square32.setFont(font)
        self.square32.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square32.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square32.setText("")
        self.square32.setObjectName("square32")
        self.square33 = QtWidgets.QPushButton(Dialog)
        self.square33.setGeometry(QtCore.QRect(300, 340, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(60)
        self.square33.setFont(font)
        self.square33.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square33.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.square33.setText("")
        self.square33.setObjectName("square33")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(240, 0, 261, 71))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 0, 0);")
        self.label.setObjectName("label")
        self.new_button = QtWidgets.QPushButton(Dialog)
        self.new_button.setGeometry(QtCore.QRect(10, 70, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.new_button.setFont(font)
        self.new_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.new_button.setObjectName("new_button")
        self.save_button = QtWidgets.QPushButton(Dialog)
        self.save_button.setGeometry(QtCore.QRect(140, 70, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.save_button.setObjectName("save_button")
        self.continue_button = QtWidgets.QPushButton(Dialog)
        self.continue_button.setGeometry(QtCore.QRect(430, 70, 160, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.continue_button.setFont(font)
        self.continue_button.setStyleSheet(
            "background-color: rgb(255, 255, 127);")
        self.continue_button.setObjectName("continue_button")
        self.Score = QtWidgets.QLabel(Dialog)
        self.Score.setGeometry(QtCore.QRect(430, 130, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Score.setFont(font)
        self.Score.setStyleSheet("color: rgb(255, 255, 0);")
        self.Score.setObjectName("Score")
        self.player_1_name = QtWidgets.QLabel(Dialog)
        self.player_1_name.setGeometry(QtCore.QRect(430, 190, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.player_1_name.setFont(font)
        self.player_1_name.setStyleSheet("color: rgb(0, 255, 255);")
        self.player_1_name.setObjectName("player_1_name")
        self.player_1_name_2 = QtWidgets.QLabel(Dialog)
        self.player_1_name_2.setGeometry(QtCore.QRect(430, 260, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.player_1_name_2.setFont(font)
        self.player_1_name_2.setStyleSheet("color: rgb(0, 255, 255);")
        self.player_1_name_2.setObjectName("player_1_name_2")
        self.Result = QtWidgets.QLabel(Dialog)
        self.Result.setGeometry(QtCore.QRect(430, 360, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.Result.setFont(font)
        self.Result.setToolTip("")
        self.Result.setStyleSheet("color:rgb(85, 255, 0)")
        self.Result.setObjectName("Result")
        self.lcdNumber = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber.setGeometry(QtCore.QRect(550, 200, 151, 41))
        self.lcdNumber.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setProperty("value", self.p1_score)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Dialog)
        self.lcdNumber_2.setGeometry(QtCore.QRect(550, 270, 151, 41))
        self.lcdNumber_2.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.lcdNumber_2.setProperty("value", self.p2_score)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.square11.clicked.connect(self.square1_1)
        self.square12.clicked.connect(self.square1_2)
        self.square13.clicked.connect(self.square1_3)
        self.square21.clicked.connect(self.square2_1)
        self.square22.clicked.connect(self.square2_2)
        self.square23.clicked.connect(self.square2_3)
        self.square31.clicked.connect(self.square3_1)
        self.square32.clicked.connect(self.square3_2)
        self.square33.clicked.connect(self.square3_3)
        self.continue_button.clicked.connect(self.continue_play)
        self.continue_button.setEnabled(False)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Tic-tac-toe"))
        self.square11.setText(_translate("Dialog", ""))
        self.square22.setText(_translate("Dialog", ""))
        self.label.setText(_translate("Dialog", "Tic-Tac-Toe"))
        self.new_button.setText(_translate("Dialog", "New Game"))
        self.save_button.setText(_translate("Dialog", "Save game"))
        self.continue_button.setText(_translate("Dialog", "Continue game"))
        self.Score.setText(_translate("Dialog", "Score:"))
        self.player_1_name.setText(_translate("Dialog", self.p1_name))
        self.player_1_name_2.setText(_translate("Dialog", self.p2_name))
        self.Result.setText(_translate("Dialog", "Result :"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
