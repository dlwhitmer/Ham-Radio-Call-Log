import sys
import os
import shutil
import sqlite3
from pathlib import Path
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
from PyQt6.QtGui import *
from PyQt6.QtCore import QSettings
from PyQt6.QtCore import QDateTime
from datetime import datetime

def get_writable_db_path():
    # Store DB in the same folder as the script
    return str(Path(__file__).parent / "Ham_Log.db")

def get_bundled_db_path():
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, 'Ham_Log.db')

# Final DB path used by the app
db_path = get_writable_db_path()

# On first run, copy bundled DB to writable location
if not os.path.exists(db_path):
    try:
        shutil.copy2(get_bundled_db_path(), db_path)
    except Exception as e:
        raise RuntimeError(f"Failed to copy database: {e}")

def prompt_callsign_if_needed(parent):
    settings = QSettings('YourCallSign', 'HamLogApp')
    callsign = settings.value('callsign', '', str)

    if not callsign.strip():
        callsign, ok = QInputDialog.getText(parent, 'Enter Call Sign', 'Please enter your call sign:')
        if ok and callsign.strip():
            callsign = callsign.strip().upper()
            settings.setValue('callsign', callsign)
    return callsign

class HamCallLog(QMainWindow):
    def __init__(self):
        super().__init__()
        prompt_callsign_if_needed(self)
        self.log_list = QListWidget()
        self.load_rows()
        self.setWindowTitle("Ham Call Log")
        self.setGeometry(100, 100, 900, 600)
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('brushednickel-2.jpg');
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: cover;
                           
            }
        """)

        menu_bar = self.menuBar()
        font = menu_bar.font()
        font.setPointSize(14)
        font.setBold(True)
        menu_bar.setFont(font)
        exit_menu = menu_bar.addMenu("Exit")
        reset_menu = menu_bar.addMenu("Reset Callsign")

        exit_action = QAction("Exit", self)
        exit_action.setFont(font)
        exit_action.triggered.connect(self.close)
        reset_action = QAction("Reset Callsign",self)
        reset_action.setFont(font)
        reset_action.triggered.connect(self.handle_callsign_reset)

        exit_menu.addAction(exit_action)
        reset_menu.addAction(reset_action)

        menu_bar.setStyleSheet("""
            QMenuBar {
                background-image: url('brushednickel-2.jpg');
                
            }
            QMenuBar::item {
                background-color: transparent;
                padding: 5px 10px;
            }
            QMenuBar::item:selected { /* Hover effect */
                background-color: #e5c185; /* Light blue */
                color: #000000;
                
            }
            QMenu {
                background-color: #c9b898;
            }
            QMenu::item {
                padding: 5px 20px;
            }
            QMenu::item:selected { /* Hover effect for menu items */
                background-color: #f1ddbf;
                color: #000000;
            }
        """)

        title_layout = QHBoxLayout()
        self.title = QLabel((f"{self.get_callsign()} Call Log"))
        self.title.setFixedSize(400,50)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFont(QFont("Arial", 24))
        title_layout.addWidget(self.title)

        label_layout = QHBoxLayout()
        self.time_stamp_label = QLabel("Time Stamp")
        self.time_stamp_label.setAlignment(Qt.AlignmentFlag.AlignCenter)    
        self.time_stamp_label.setFixedSize(150,30)
        self.time_stamp_label.setStyleSheet("background-color: #ffffea; font-size: 18px;font-weight: 600; border: 2px solid #000; border-radius: 10px;")
        self.callsign_label = QLabel("Callsign")
        self.callsign_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.callsign_label.setFixedSize(150,30)
        self.callsign_label.setStyleSheet("background-color: #ffffea; font-size: 18px;font-weight: 600; border: 2px solid #000; border-radius: 10px;")
        self.frequency_label = QLabel("Frequency")
        self.frequency_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frequency_label.setFixedSize(100,30)
        self.frequency_label.setStyleSheet("background-color: #ffffea; font-size: 18px;font-weight: 600; border: 2px solid #000; border-radius: 10px;")
        self.mode_label = QLabel("Mode")
        self.mode_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.mode_label.setFixedSize(100,30)
        self.mode_label.setStyleSheet("background-color: #ffffea; font-size: 18px;font-weight: 600; border: 2px solid #000; border-radius: 10px;")
        self.location_label = QLabel("Location")
        self.location_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.location_label.setFixedSize(150,30)
        self.location_label.setStyleSheet("background-color: #ffffea; font-size: 18px;font-weight: 600; border: 2px solid #000; border-radius: 10px;")
        

        input_layout = QHBoxLayout()
        self.time_stamp = QLineEdit()
        self.time_stamp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_stamp.setFixedSize(150,30)
        self.time_stamp.setStyleSheet("background-color: #f1ddbf; border: 1px solid gray; font-size: 14px;font-weight: bold;")
        self.callsign_input = QLineEdit()
        self.callsign_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.callsign_input.setFixedSize(150,30)
        self.callsign_input.setStyleSheet("background-color: #f1ddbf; border: 1px solid gray; font-size: 14px;font-weight: bold;")
        self.frequency_input = QLineEdit()
        self.frequency_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frequency_input.setFixedSize(100,30)
        self.frequency_input.setStyleSheet("background-color: #f1ddbf; border: 1px solid gray; font-size: 14px;font-weight: bold;")
        self.mode_combo = QComboBox()
        self.mode_combo.setEditable(True)
        self.mode_combo.setFixedSize(100,30)
        self.mode_combo.setStyleSheet("background-color: #f1ddbf; border: 1px solid gray; font-size: 14px;font-weight: bold;")
        self.mode_combo.addItems(["SSB", "CW", "FM", "AM", "Digital"])
        self.mode_combo.lineEdit().setAlignment(Qt.AlignmentFlag.AlignCenter)  # Center-align text
        # self.mode_combo.
        self.location_input = QLineEdit() 
        self.location_input.setAlignment(Qt.AlignmentFlag.AlignCenter)  
        self.location_input.setFixedSize(150,30)
        self.location_input.setStyleSheet("background-color: #f1ddbf; border: 1px solid gray; font-size: 14px; font-weight: bold;")
        label_layout.addWidget(self.time_stamp_label)
        label_layout.addWidget(self.callsign_label)
        label_layout.addWidget(self.frequency_label)
        label_layout.addWidget(self.mode_label)
        label_layout.addWidget(self.location_label)

        input_layout.addWidget(self.time_stamp)
        input_layout.addWidget(self.callsign_input)
        input_layout.addWidget(self.frequency_input)
        input_layout.addWidget(self.mode_combo)
        input_layout.addWidget(self.location_input)

        log_layout = QHBoxLayout()
        self.log_list.setStyleSheet("background-color: #f1ddbf; border: 1px solid gray; font-size: 14px; font-weight: 500;")
        log_layout.addWidget(self.log_list)
        btn_layout = QHBoxLayout()
        self.add_button = QPushButton("Add Entry")
        btn_layout.addStretch(1)
        btn_layout.addWidget(self.add_button)
        btn_layout.addStretch(1)
        self.add_button.clicked.connect(self.add_entry)
        self.add_button.setFixedSize(100,30)
        self.add_button.setStyleSheet("background-color: #a3c1ad; border: 1px solid gray; font-size: 14px;font-weight: bold;")
        btn_layout.addStretch()

        layout.addLayout(title_layout)
        layout.addLayout(label_layout)
        layout.addLayout(input_layout)
        layout.addLayout(log_layout)
        layout.addLayout(btn_layout)


    # 
    def add_entry(self):
       self.time_stamp.setText(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
       time = self.time_stamp.text().strip().upper()
       callsign = self.callsign_input.text().strip().upper()
       frequency = self.frequency_input.text().strip().upper()
       mode = self.mode_combo.currentText().upper()
       location = self.location_input.text().strip().upper()

       conn = sqlite3.connect(get_writable_db_path())
       c = conn.cursor()
       c.execute("""
           INSERT INTO Call_Log (Time_Stamp, Callsign, Frequency, Mode, Location)
           VALUES (?, ?, ?, ?, ?)
       """, (time, callsign, frequency, mode, location))
       conn.commit()
       conn.close()
       self.time_stamp.clear()
       self.callsign_input.clear()
       self.frequency_input.clear()
       self.location_input.clear()  
       self.load_rows()

    def load_rows(self):
        self.log_list.clear()
        conn = sqlite3.connect(get_writable_db_path())
        c = conn.cursor()
        c.execute("SELECT ID, Time_Stamp, Callsign, Frequency, Mode, Location FROM Call_Log ORDER BY Time_Stamp DESC")
        rows = c.fetchall()
        conn.close()
        for row in rows:
            self.add_log_row(row)

    def add_log_row(self, row):
        log_id, time_stamp, callsign, frequency, mode, location = row
        item_widget = QWidget()
        item_layout = QHBoxLayout(item_widget)
        item_layout.setContentsMargins(5, 5, 5, 5)  
        time_label = QLabel(time_stamp)
        time_label.setFixedSize(150,30)
        time_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        time_label.setStyleSheet("background-color: #003f5c; color:white;font-size: 15px; font-weight:600;")   
        callsign_label = QLabel(callsign)
        callsign_label.setFixedSize(150,30)
        callsign_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        callsign_label.setStyleSheet("background-color: #003f5c; color:white;font-size: 15px; font-weight:600;")  
        frequency_label = QLabel(frequency)
        frequency_label.setFixedSize(100,30)
        frequency_label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
        frequency_label.setStyleSheet("background-color: #003f5c; color:white;font-size: 15px; font-weight:600;")  
        mode_label = QLabel(mode)
        mode_label.setFixedSize(100,30)
        mode_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mode_label.setStyleSheet("background-color: #003f5c; color:white;font-size: 15px; font-weight:600;")   
        location_label = QLabel(location)
        location_label.setFixedSize(150,30)
        location_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        location_label.setStyleSheet("background-color: #003f5c; color:white;font-size: 15px; font-weight:600;")   
        edit_button = QPushButton("Edit")
        edit_button.setFixedSize(60,30)
        edit_button.setStyleSheet("background-color: #f0ad4e; border: 1px solid gray; font-size: 12px; font-weight: bold;")
        edit_button.clicked.connect(lambda _, log_id=log_id: self.edit_selected_log(log_id))
        delete_button = QPushButton("Delete")
        delete_button.setFixedSize(60,30)
        delete_button.setStyleSheet("background-color: #d9534f; border: 1px solid gray; font-size: 12px; font-weight: bold; color: white;")
        delete_button.clicked.connect(lambda _, log_id=log_id: self.delete_row_by_id(log_id))
        item_layout.addWidget(time_label)
        item_layout.addWidget(callsign_label)
        item_layout.addWidget(frequency_label)
        item_layout.addWidget(mode_label)
        item_layout.addWidget(location_label)
        item_layout.addWidget(edit_button)
        item_layout.addWidget(delete_button)
        list_item = QListWidgetItem(self.log_list)
        list_item.setSizeHint(item_widget.sizeHint())
        self.log_list.addItem(list_item)
        self.log_list.setItemWidget(list_item, item_widget)

    
    def delete_row_by_id(self, log_id):
        confirm = QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this log entry?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)   
        if confirm == QMessageBox.StandardButton.Yes:
            conn = sqlite3.connect(get_writable_db_path())
            c = conn.cursor()
            c.execute("DELETE FROM Call_Log WHERE ID = ?", (log_id,))
            conn.commit()
            conn.close()
            self.load_rows()

    def edit_selected_log(self, log_id):
        conn = sqlite3.connect(get_writable_db_path())
        c = conn.cursor()
        c.execute("SELECT Time_Stamp, Callsign, Frequency, Mode, Location FROM Call_Log WHERE ID = ?", (log_id,))
        row = c.fetchone()
        conn.close()    
        if row:
            time_stamp, callsign, frequency, mode, location = row
            dialog = QDialog(self)
            dialog.setWindowTitle("Edit Log Entry")
            dialog.setFixedSize(400, 300)
            layout = QVBoxLayout(dialog)
            time_input = QLineEdit(time_stamp)
            time_input.setReadOnly(True)
            time_input.setStyleSheet("background-color: #f0f0f0; color: #555;")
            callsign_input = QLineEdit(callsign)
            frequency_input = QLineEdit(frequency)
            mode_combo = QComboBox()
            mode_combo.addItems(["SSB", "CW", "FM", "AM", "Digital"])
            mode_index = mode_combo.findText(mode)
            if mode_index >= 0:
                mode_combo.setCurrentIndex(mode_index)
            location_input = QLineEdit(location)
            layout.addWidget(QLabel("Time Stamp:"))
            layout.addWidget(time_input)
            layout.addWidget(QLabel("Callsign:"))
            layout.addWidget(callsign_input)
            layout.addWidget(QLabel("Frequency:"))
            layout.addWidget(frequency_input)
            layout.addWidget(QLabel("Mode:"))
            layout.addWidget(mode_combo)
            layout.addWidget(QLabel("Location:"))
            layout.addWidget(location_input)
            button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel)
            layout.addWidget(button_box)
            button_box.accepted.connect(dialog.accept)
            button_box.rejected.connect(dialog.reject)
            # Execute dialog
        if dialog.exec() == QDialog.DialogCode.Accepted:
            # new_time = time_input.text().strip()
            new_callsign = callsign_input.text().strip().upper()
            new_frequency = frequency_input.text().strip().upper()
            new_mode = mode_combo.currentText().upper()
            new_location = location_input.text().strip().upper()

            # Update database
            conn = sqlite3.connect(get_writable_db_path())
            c = conn.cursor()
            c.execute("""
                UPDATE Call_Log
                SET Callsign = ?, Frequency = ?, Mode = ?, Location = ?
                WHERE ID = ?
            """, (new_callsign, new_frequency, new_mode, new_location, log_id))
            conn.commit()
            conn.close()

            # Optional: refresh UI or notify user
            self.load_rows()            

    def get_callsign(self):
         settings = QSettings('YourCallSign', 'HamCallLog')
         return settings.value('callsign', 'WB3JWL', str)

    def handle_callsign_reset(self):
        print("Reset triggered")  # 🔍 Confirm it's firing
        settings = QSettings('YourCallSign', 'HamLogApp')
        settings.remove('callsign')  # ⬅️ Clears it out
        # Prompt again right after reset
        edited_callsign = prompt_callsign_if_needed(self)
        self.title.setText(f"{edited_callsign} Call Log")

    def update_title(self):
        callsign = self.get_callsign()
        self.title.setText(f"{callsign} Call Log")



app = QApplication(sys.argv)
window = HamCallLog()
window.show()
sys.exit(app.exec())