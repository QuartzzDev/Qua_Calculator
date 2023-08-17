# Quartzz <3

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Quartzz Hesap Makinesi')

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.result_display)

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C']
        ]

        for row in buttons:
            button_row = QHBoxLayout()
            for button_text in row:
                button = QPushButton(button_text)
                button.clicked.connect(self.button_click)
                button_row.addWidget(button)
            layout.addLayout(button_row)

        self.setLayout(layout)

        self.current_expression = ''

    def button_click(self):
        clicked_button = self.sender()
        button_text = clicked_button.text()

        if button_text == '=':
            try:
                result = str(eval(self.current_expression))
                self.result_display.setText(result)
                self.current_expression = result
            except Exception as e:
                self.result_display.setText('Hata')
                self.current_expression = ''
        elif button_text == 'C':
            self.result_display.clear()
            self.current_expression = ''
        else:
            self.current_expression += button_text
            self.result_display.setText(self.current_expression)

def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
