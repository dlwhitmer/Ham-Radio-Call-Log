import sys
import serial
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from morsely import MorseDecoder



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.value = 600  # Initial delay value (e.g., in milliseconds)
        self.step = 10    # Step size for increment/decrement
        self.setWindowTitle("Ham Radio Log")
        self.setGeometry(150, 50, 1200, 700)
        self.setStyleSheet("background-color:#dde5b4;")

        self.initUI()

    def initUI(self):
        # Main layout
        layout = QVBoxLayout() 

        #Tile Label
        title_layout = QHBoxLayout()
        self.title = QLabel("WB3JWL Ham Log")
        self.title.setFixedSize(400,50)
        self.title.setStyleSheet("background-color:#adc178; font-family: Arial;  font-size: 40px; font-weight: 800;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_layout.addWidget(self.title)

        # TextEdits
        snd_layout = QVBoxLayout()
        self.snd = QLineEdit()
        self.snd.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.snd.setStyleSheet("background-color: lightblue;font-size: 20px; font-weight: 700;")
        self.snd.setPlaceholderText("This is where you type the message and Press 'Send'")
        self.snd.setFixedHeight(250)
        snd_layout.addWidget(self.snd)

        label_layout = QHBoxLayout()
        label_layout2 = QHBoxLayout()
        self.label = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel("WPM")
        self.label4 = QLabel("Delay Rate")
        self.label3.setStyleSheet(" font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px; ")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label3.setFixedSize(150,30)
        self.label4.setFixedSize(150,30)
        self.label4.setStyleSheet(" font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px;")
        label_layout2.addWidget(self.label3)
        label_layout2.addWidget(self.label4)
        self.label.setFixedSize(150,30)
        self.label.setStyleSheet("background-color: #fdffb6; font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px;")
        label_layout.addWidget(self.label)
        label_layout.addWidget(self.label2)
        self.label2.setFixedSize(150,30)
        self.label2.setStyleSheet("background-color: #fdffb6; font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px;")
        label_layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
        label_layout2.setAlignment(Qt.AlignmentFlag.AlignJustify)

        self.speed_slider = QSlider()
        slider_layout = QHBoxLayout()
        self.speed_slider.setMinimum(50)
        self.speed_slider.setMaximum(200)
        self.speed_slider.setValue(200)
        self.speed_slider.setOrientation(Qt.Orientation.Horizontal)  # or Qt.Orientation.Vertical
        self.speed_slider.setInvertedAppearance(True)  # Reverse the slider
        self.speed_slider.valueChanged.connect(lambda value: self.convert_to_wpm(value))
        self.speed_slider.valueChanged.connect(lambda value: self.update_label2(value))

        # self.slider.valueChanged.connect(lambda value:self.convert_to_wpm(value))
        slider_layout.addWidget(self.speed_slider)

        button_layout = QHBoxLayout()
        button_layout.setAlignment(Qt.AlignmentFlag.AlignJustify)
        
        self.conn = QPushButton("Connect\nTo Arduino")
        self.conn.clicked.connect(self.connect_to_arduino)
        self.conn.setFixedSize(200,47)
        self.conn.setStyleSheet("background-color:#f1ddbf;font-size: 18px;font-weight:700; border: 2px solid #413344; border-radius: 15px; margin: 0 10 0 10;")

        self.send = QPushButton("Send")
        self.send.clicked.connect(self.send_text)
        self.send.setFixedSize(200,47)
        self.send.setStyleSheet("background-color:#f1ddbf;font-size: 18px;font-weight:700; border: 2px solid #413344; border-radius: 15px; margin: 0 10 0 10;")
        self.Receive = QPushButton("Receive")
        self.Receive.clicked.connect(self.receive_code)
        self.Receive.setStyleSheet("background-color:#f1ddbf;font-size: 18px;font-weight:700; border: 2px solid #413344; border-radius: 15px; margin: 0 10 0 10;")
        self.Receive.setFixedSize(200,47)
        self.clear = QPushButton("Clear The\nScreens")
        self.clear.clicked.connect(self.clear_the_screens)
        self.clear.setFixedSize(200,47)
        self.clear.setStyleSheet("background-color:#f1ddbf;font-size: 18px;font-weight:700; border: 2px solid #413344; border-radius: 15px; margin: 0 10 0 10;")

        button_layout.addWidget(self.conn)
        button_layout.addWidget(self.send)
        button_layout.addWidget(self.Receive)
        button_layout.addWidget(self.clear)

        rx_layout = QVBoxLayout()
        self.rx = QLineEdit()
        self.rx.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.rx.setStyleSheet("background-color: lightblue;font-size: 20px; font-weight: 700;")
        self.rx.setPlaceholderText("This is where you Press 'Receive Button' and receive converted Morse Code")
        self.rx.setFixedHeight(250)
        rx_layout.addWidget(self.rx)

        layout.addLayout(title_layout)
        layout.addLayout(snd_layout)
        layout.addLayout(label_layout2)
        layout.addLayout(label_layout)
        layout.addLayout(slider_layout)
        layout.addLayout(button_layout)
        layout.addLayout(rx_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def clear_the_screens(self):
        self.snd.clear()
        self.rx.clear()

    def update_label2(self, value):
        self.label2.setText(f"{value:.2f}")


    def connect_to_arduino(self):
        """Establish a connection to the Arduino."""
        try:
            # Replace 'COM3' with your Arduino's port and set the correct baud rate
            self.arduino = serial.Serial('COM5', 9600, timeout=1)
            if self.arduino:
                self.conn.setStyleSheet("background-color:#72b043;font-size: 18px;font-weight:700; border: 2px solid #413344; border-radius: 15px; margin: 0 10 0 10;")
            else:
                QMessageBox.warning(None, "Connection Failed", "Failed to open the serial port.")
                self.conn.setStyleSheet("background-color:#e12729;font-size: 18px;font-weight:700; border: 2px solid #413344; border-radius: 15px; margin: 0 10 0 10;")
        except serial.SerialException as e:
            QMessageBox.critical(None, "Error", f"Could not connect to Arduino: {e}")
        
        except serial.SerialException as e:
            print(f"Error connecting to Arduino: {e}")
            return None

    def convert_to_wpm(self, value):
        try:
            unit_duration_ms = float(f"{value}")
            wpm = 1200 / unit_duration_ms
            self.label.setText(f"{wpm:.2f}")
        
        except ValueError:
            self.result_display.setText("Invalid input. Please enter a number.")

    def send_text(self):
        text = self.snd.text()
        speed = self.speed_slider.value()
        message = f"{speed}:{text}\n"
        self.arduino.write(message.encode())

    def receive_code(self):
        decoder = MorseDecoder()
        decoding_results = decoder.decode_wav_file("message.wav")
        self.rx.setText(decoding_results.morse_decoded_text) #.... . .-.. .-.. --- --..-- / .-- --- .-. .-.. -.. -.-.--
        self.rx.setText(decoding_results.latin_decoded_text) #HELLO, WORLD!
    
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec())    
