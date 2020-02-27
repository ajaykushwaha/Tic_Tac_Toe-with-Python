# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_game.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_game(object):
    def setupUi(self, new_game):
        new_game.setObjectName("new_game")
        new_game.resize(537, 304)
        new_game.setStyleSheet("background-color: rgb(152, 152, 114);")
        self.start_button = QtWidgets.QPushButton(new_game)
        self.start_button.setGeometry(QtCore.QRect(400, 220, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.start_button.setFont(font)
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start_button.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.start_button.setObjectName("start_button")
        self.radioButton_1 = QtWidgets.QRadioButton(new_game)
        self.radioButton_1.setGeometry(QtCore.QRect(70, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_2 = QtWidgets.QRadioButton(new_game)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 110, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.game_combo = QtWidgets.QComboBox(new_game)
        self.game_combo.setGeometry(QtCore.QRect(200, 100, 321, 31))
        self.game_combo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.game_combo.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.game_combo.setObjectName("game_combo")
        self.lineEdit = QtWidgets.QLineEdit(new_game)
        self.lineEdit.setGeometry(QtCore.QRect(140, 180, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(new_game)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 240, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.player_1_name_2 = QtWidgets.QLabel(new_game)
        self.player_1_name_2.setGeometry(QtCore.QRect(20, 170, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.player_1_name_2.setFont(font)
        self.player_1_name_2.setStyleSheet("color: rgb(255, 255, 0);")
        self.player_1_name_2.setObjectName("player_1_name_2")
        self.player_1_name_3 = QtWidgets.QLabel(new_game)
        self.player_1_name_3.setGeometry(QtCore.QRect(20, 220, 91, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.player_1_name_3.setFont(font)
        self.player_1_name_3.setStyleSheet("color: rgb(255, 255,0);")
        self.player_1_name_3.setObjectName("player_1_name_3")

        self.retranslateUi(new_game)
        QtCore.QMetaObject.connectSlotsByName(new_game)

    def retranslateUi(self, new_game):
        _translate = QtCore.QCoreApplication.translate
        new_game.setWindowTitle(_translate("new_game", "New Game"))
        self.start_button.setText(_translate("new_game", "Start"))
        self.radioButton_1.setText(_translate("new_game", "New Game"))
        self.radioButton_2.setText(_translate("new_game", "Load Game"))
        self.player_1_name_2.setText(_translate("new_game", "Player 1"))
        self.player_1_name_3.setText(_translate("new_game", "player 2"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    new_game = QtWidgets.QDialog()
    ui = Ui_new_game()
    ui.setupUi(new_game)
    new_game.show()
    sys.exit(app.exec_())

