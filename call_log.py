import sys
import csv
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from datetime import datetime

class HamLog(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ham Radio Log")
        self.setGeometry(150, 50, 1200, 700)
        self.setStyleSheet("background-color:#dde5b4;")

        self.initUI()

    def initUI(self):
        # Main layout
        layout = QVBoxLayout()     

        font = QFont("Arial",25)
        font.setBold(True)
          
        #Title
        title_layout = QHBoxLayout()
        self.title = QLabel("WB3JWL Call Log")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFixedSize(400,50)
        self.title.setStyleSheet(" background-color: #000;color: #f8cc1b; font-size: 40px; font-weight: 700; border-radius: 20px;")
        title_layout.addWidget(self.title, alignment=(Qt.AlignmentFlag.AlignCenter))

        # Input fields
        input_layout = QHBoxLayout()
        self.time_stamp_input = QLineEdit()
        self.time_stamp_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_stamp_input.setFixedSize(200,40)
        self.time_stamp_input.setStyleSheet("background-color:#adc178; font-size: 18px; font-weight: 800;")
        self.time_stamp_input.setPlaceholderText("Time Stamp")
        self.callsign_input = QLineEdit()
        self.callsign_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.callsign_input.setFixedSize(200,40)
        self.callsign_input.setStyleSheet("background-color:#adc178; font-size: 18px; font-weight: 800;")
        self.callsign_input.setPlaceholderText("Callsign")
        self.frequency_input = QLineEdit()
        self.frequency_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frequency_input.setFixedSize(200,40)
        self.frequency_input.setStyleSheet("background-color:#adc178; font-size: 18px; font-weight: 800;")
        self.frequency_input.setPlaceholderText("Frequency")
        self.mode_input = QLineEdit()
        self.mode_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mode_input.setFixedSize(200,40)
        self.mode_input.setStyleSheet("background-color:#adc178; font-size: 18px; font-weight: 800;")
        self.mode_input.setPlaceholderText("Mode")
        self.location_input = QLineEdit()
        self.location_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.location_input.setFixedSize(300,40)
        self.location_input.setStyleSheet("background-color:#adc178; font-size: 18px; font-weight: 800;")
        self.location_input.setPlaceholderText("Location")
        input_layout.addWidget(self.time_stamp_input)
        input_layout.addWidget(self.callsign_input)
        input_layout.addWidget(self.frequency_input)
        input_layout.addWidget(self.mode_input)
        input_layout.addWidget(self.location_input)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
        self.add_button = QPushButton("Add To Log")
        self.add_button.setFixedSize(200,40)
        self.add_button.setStyleSheet("background-color: #000; font-size: 22px; font-weight: 700; border-radius: 15px; color:#ffa600;")
        self.add_button.clicked.connect(self.add_entry)
        self.save_button = QPushButton("Save Log")
        self.save_button.setFixedSize(200,40)
        self.save_button.setStyleSheet("background-color: #000; font-size: 22px; font-weight: 700; border-radius: 15px; color:#ffa600;")
        self.save_button.clicked.connect(self.save_log)
        self.load_button = QPushButton("Load Log")
        self.load_button.setFixedSize(200,40)
        self.load_button.setStyleSheet("background-color: #000; font-size: 22px; font-weight: 700; border-radius: 15px; color:#ffa600;")
        self.load_button.clicked.connect(self.load_log)
        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.load_button)

        
        table_layout = QHBoxLayout()
        self.table = QTableWidget()
        table_layout.addWidget(self.table)
        self.table.setStyleSheet("background-color: #f0ead2; font-family: Arial; font-size: 18px; font-weight: 800; background-color:#f0ead2;border: 2px solid #000; color:#000;")
        self.table.setColumnCount(5)
        self.table.setColumnWidth(0, 200)
        self.table.setColumnWidth(1, 200)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnWidth(3, 200)
        self.table.setColumnWidth(4, 300)
        self.table.setHorizontalHeaderLabels(["Time Stamp","Callsign", "Frequency", "Mode", "Location"])

        # Add widgets to layout
        layout.addLayout(title_layout)
        layout.addLayout(input_layout)
        layout.addLayout(button_layout)
        layout.addLayout(table_layout)

        # Set central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


    def add_entry(self):
        time = datetime.now().strftime("%Y-%m-%d %H:%M")
        callsign = self.callsign_input.text().upper()
        frequency = self.frequency_input.text().upper()
        mode = self.mode_input.text().upper()
        location = self.location_input.text().upper()

        if time and callsign and frequency and mode :
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(time))
            self.table.setItem(row_position, 1, QTableWidgetItem(callsign))
            self.table.setItem(row_position, 2, QTableWidgetItem(frequency))
            self.table.setItem(row_position, 3, QTableWidgetItem(mode))
            self.table.setItem(row_position, 4, QTableWidgetItem(location))

            # Clear input fields
            self.time_stamp_input.clear()
            self.callsign_input.clear()
            self.frequency_input.clear()
            self.mode_input.clear()
            self.location_input.clear()
    def save_log(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save Log", "", "CSV Files (*.csv)")
        if path:
            with open(path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Time Stamp", "Callsign", "Frequency", "Mode", "Location"])
                for row in range(self.table.rowCount()):
                    writer.writerow([
                        self.table.item(row, 0).text(),
                        self.table.item(row, 1).text(),
                        self.table.item(row, 2).text(),
                        self.table.item(row, 3).text(),
                        self.table.item(row, 4).text()
                    ])

    def load_log(self):
        path, _ = QFileDialog.getOpenFileName(self, "Load Log", "", "CSV Files (*.csv)")
        if path:
            with open(path, mode='r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                self.table.setRowCount(0)  # Clear existing rows
                for row_data in reader:
                    row_position = self.table.rowCount()
                    self.table.insertRow(row_position)
                    for column, data in enumerate(row_data):
                        self.table.setItem(row_position, column, QTableWidgetItem(data))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HamLog()
    window.show()
    sys.exit(app.exec())