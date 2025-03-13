import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton, 
    QComboBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class Connect4IntroUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Connect 4")  # Title in the top bar
        self.setGeometry(100, 100, 400, 350)  # Window size, coordinates on screen
        self.setStyleSheet("background-color: white;")  # White background

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Align elements to the top

        # Title Label Inside Window
        title = QLabel("Connect 4", self)
        title.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("color: black; margin-bottom: 20px;")  # Ensure text is visible
        layout.addWidget(title)

        # Name Input
        self.name_label = QLabel("Name:", self)
        self.name_label.setFont(QFont("Arial", 12))
        self.name_label.setStyleSheet("color: black;")  # Ensure text is visible
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter your name")
        # self.name_input.setText("Test")  # Default value
        self.name_input.setStyleSheet("color: black; background-color: white;")  

        # Difficulty Level Dropdown
        self.difficulty_label = QLabel("Difficulty Level:", self)
        self.difficulty_label.setFont(QFont("Arial", 12))
        self.difficulty_label.setStyleSheet("color: black;")
        self.difficulty_dropdown = QComboBox(self)
        self.difficulty_dropdown.addItems(["Easy", "Normal", "Hard"])
        self.difficulty_dropdown.setStyleSheet("color: black; background-color: white;")  
        # Game Narrative Theme Dropdown
        self.theme_label = QLabel("Game Narrative Theme:", self)
        self.theme_label.setFont(QFont("Arial", 12))
        self.theme_label.setStyleSheet("color: black;")
        self.theme_dropdown = QComboBox(self)
        self.theme_dropdown.addItems(["Western", "Civil War", "Fantasy", "Harry Potter"])
        self.theme_dropdown.setStyleSheet("color: black; background-color: white;")

        # AI Personality Dropdown
        self.ai_label = QLabel("AI Personality:", self)
        self.ai_label.setFont(QFont("Arial", 12))
        self.ai_label.setStyleSheet("color: black;")
        self.ai_dropdown = QComboBox(self)
        self.ai_dropdown.addItems(["Snarky", "Aggressive", "Encouraging"])
        self.ai_dropdown.setStyleSheet("color: black; background-color: white;") 

        # Start Game Button
        self.start_button = QPushButton("Start Game", self)
        self.start_button.setStyleSheet("""
            QPushButton {
                background-color: lightblue; 
                font-size: 14px; 
                padding: 10px;
                border-radius: 5px;
                color: black;
            }
            QPushButton:hover {
                background-color: #87CEEB;
            }
        """)
        self.start_button.clicked.connect(self.start_game)

        # Add Widgets to Layout
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.difficulty_label)
        layout.addWidget(self.difficulty_dropdown)
        layout.addWidget(self.theme_label)
        layout.addWidget(self.theme_dropdown)
        layout.addWidget(self.ai_label)
        layout.addWidget(self.ai_dropdown)
        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def start_game(self):
        """ Collects user input and starts the game """
        name = self.name_input.text()
        difficulty = self.difficulty_dropdown.currentText()
        theme = self.theme_dropdown.currentText()
        ai_personality = self.ai_dropdown.currentText()

        print(f"Starting game with:\nName: {name}\nDifficulty: {difficulty}\nTheme: {theme}\nAI Personality: {ai_personality}")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    window = Connect4IntroUI()
    window.show()
    sys.exit(app.exec())
