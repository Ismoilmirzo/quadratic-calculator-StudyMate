import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5 import QtGui
from PyQt5.QtGui import QFont, QColor, QPalette, QDoubleValidator
from PyQt5.QtCore import Qt


class StudyMateApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("StudyMate")
        self.setWindowIcon(QtGui.QIcon('rasm.png'))
        self.setGeometry(100, 100, 450, 300)

        self.init_ui()

    def init_ui(self):
        self.title_label = QLabel("Quadratic Formula Calculator", self)
        self.title_label.setGeometry(20, 20, 360, 40)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.title_label.setStyleSheet("color: white; background-color: #357DED;")


        
        self.general_formula_label = QLabel("General Formula: ax² + bx + c = 0", self)
        self.general_formula_label.setGeometry(20, 50, 300, 30)
        self.general_formula_label.setStyleSheet("font-size: 10pt;")

        self.a_label = QLabel("a =", self)
        self.a_label.setGeometry(20, 80, 20, 20)
        self.a_input = QLineEdit(self)
        self.a_input.setGeometry(50, 80, 50, 20)
        self.a_input.setValidator(QDoubleValidator())
        
        self.b_label = QLabel("b =", self)
        self.b_label.setGeometry(20, 110, 20, 20)
        self.b_input = QLineEdit(self)
        self.b_input.setGeometry(50, 110, 50, 20)
        self.b_input.setValidator(QDoubleValidator())
        
        self.c_label = QLabel("c =", self)
        self.c_label.setGeometry(20, 140, 20, 20)
        self.c_input = QLineEdit(self)
        self.c_input.setGeometry(50, 140, 50, 20)
        self.c_input.setValidator(QDoubleValidator())

        self.clear_button = QPushButton("Clear", self)
        self.clear_button.setGeometry(20, 180, 75, 30)
        self.clear_button.clicked.connect(self.clear_inputs)
        self.clear_button.setStyleSheet("background-color: #FF5050; color: white; font-weight: bold;")

        self.calculate_button = QPushButton("Calculate", self)
        self.calculate_button.setGeometry(110, 180, 75, 30)
        self.calculate_button.clicked.connect(self.calculate_quadratic_formula)
        self.calculate_button.setStyleSheet("background-color: #50C878; color: white; font-weight: bold;")

        self.answer_label = QLabel("Answer:", self)
        self.answer_label.setGeometry(20, 240, 500, 30)
        self.answer_label.setStyleSheet("font-size: 10pt;")

        self.menu = self.menuBar()
        self.organisation_menu = self.menu.addMenu("Our Organisation")
        self.website_action = self.organisation_menu.addAction("Website")
        self.website_action.triggered.connect(self.open_website)
        
    def clear_inputs(self):
        self.a_input.clear()
        self.b_input.clear()
        self.c_input.clear()
        self.answer_label.clear()

    def calculate_quadratic_formula(self):
        a = float(self.a_input.text())
        b = float(self.b_input.text())
        c = float(self.c_input.text())

        discriminant = b**2 - 4*a*c
        if a == 0:
            QMessageBox.warning(self, "Error", "a cannot be 0.")
            self.a_input.clear()
            return
        if discriminant >= 0:
            x1 = (-b + discriminant ** 0.5) / (2 * a)
            x2 = (-b - discriminant ** 0.5) / (2 * a)
            answer = f"x1 = {x1:.6f}, x2 = {x2:.6f}"
        else:
            real_part = -b / (2 * a)
            imaginary_part = (-discriminant) ** 0.5 / (2 * a)
            answer = f"x1 = {real_part:.6f} + {imaginary_part:.6f}i, x2 = {real_part:.6f} - {imaginary_part:.6f}i"

        self.answer_label.setText(f"Answer: {answer}")


    def open_website(self):
        import webbrowser
        webbrowser.open("https://matestudy.netlify.app")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StudyMateApp()
    window.show()
    sys.exit(app.exec_())
