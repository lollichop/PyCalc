# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDialog
from PyQt5 import QtCore
from ui import UserInterface


class Main(QDialog):
    def __init__(self):
        super().__init__()

        self.ui = UserInterface()
        self.ui.initialize_ui(self)

        self.result = None

        self.text_expression_data = ''

        self.ui.button_one.clicked.connect(lambda: self.button_clicked('1'))
        self.ui.button_two.clicked.connect(lambda: self.button_clicked('2'))
        self.ui.button_three.clicked.connect(lambda: self.button_clicked('3'))
        self.ui.button_four.clicked.connect(lambda: self.button_clicked('4'))
        self.ui.button_five.clicked.connect(lambda: self.button_clicked('5'))
        self.ui.button_six.clicked.connect(lambda: self.button_clicked('6'))
        self.ui.button_seven.clicked.connect(lambda: self.button_clicked('7'))
        self.ui.button_eight.clicked.connect(lambda: self.button_clicked('8'))
        self.ui.button_nine.clicked.connect(lambda: self.button_clicked('9'))
        self.ui.button_zero.clicked.connect(lambda: self.button_clicked('0'))
        self.ui.button_plus.clicked.connect(lambda: self.button_clicked('+'))
        self.ui.button_minus.clicked.connect(lambda: self.button_clicked('-'))
        self.ui.button_divide.clicked.connect(lambda: self.button_clicked('/'))
        self.ui.button_multiply.clicked.connect(lambda: self.button_clicked('*'))

        self.ui.text_expression.returnPressed.connect(self.evaluate_expression)

        self.ui.button_c.clicked.connect(self.button_clicked_clear)
        self.ui.button_backspace.clicked.connect(self.button_clicked_backspace)

        self.ui.button_equals.clicked.connect(self.evaluate_expression)

        self.show()

    def button_clicked(self, text):
        self.text_expression_data += text
        self.ui.text_expression.setText(self.text_expression_data)

    def button_clicked_backspace(self):
        self.text_expression_data = self.text_expression_data[:-1]
        self.ui.text_expression.setText(self.text_expression_data)

    def button_clicked_clear(self):
        self.text_expression_data = ''
        self.ui.text_expression.setText(self.text_expression_data)

    def evaluate_expression(self):
        if '/cmd' in self.text_expression_data:
            self.evaluate_command()

        # Get text from the text field.
        self.text_expression_data = self.ui.text_expression.text()

        self.result = eval(self.text_expression_data)
        self.display_result(self.result)

    def evaluate_command(self):
        pass

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key == QtCore.Qt.Key_Return:
            print("PRESSED")

    def display_result(self, result):
        # self.ui.text_expression.setFontPointSize(20)
        self.ui.text_expression.setText(str(result))
        self.text_expression_data = str(result)
    
app = QApplication(sys.argv)
w = Main()
w.show()
sys.exit(app.exec_())