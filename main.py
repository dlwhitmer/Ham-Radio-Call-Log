import sys
import serial
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from morsely import MorseDecoder
import sounddevice as sd
import soundfile as sf

class RecorderThread(QThread):
    recording_stopped = pyqtSignal()

    def __init__(self, filename, samplerate=44100, channels=2):
        super().__init__()
        self.filename = filename
        self.samplerate = samplerate
        self.channels = channels
        self.is_recording = False

    def run(self):
        self.is_recording = True
        with sf.SoundFile(self.filename, mode='w', samplerate=self.samplerate,
                          channels=self.channels) as file:
            with sd.InputStream(samplerate=self.samplerate, channels=self.channels,
                                callback=lambda indata, frames, time, status: self.callback(indata, file)):
                while self.is_recording:
                    sd.sleep(100)

    def callback(self, indata, file):
        if self.is_recording:
            file.write(indata)

    def stop(self):
        self.is_recording = False
        self.recording_stopped.emit()



class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.recorder_thread = None

        self.is_recording = False
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
        self.title = QLabel("WB3JWL Call Log")
        self.title.setFixedSize(400,50)
        self.title.setStyleSheet("background-color:#adc178; font-family: Arial;  font-size: 40px; font-weight: 800;border: 2px solid #000; border-radius: 20px;")
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_layout.addWidget(self.title)

        self.combo = QComboBox()
        self.combo.setPlaceholderText("Common Used Phrases")
        self.combo.addItems(["CQ CQ CQ WB3JWL ", "        MY NAME IS DAN  AND MY QTH IS CLINTONVILLE PA ", "YOUR RST IS 599", "WHAT IS YOUR QTH ", "MY NAME IS DAN ","  THIS IS WB3JWL"])
        self.combo.currentTextChanged.connect(self.update_text_edit)
        
        combo_layout =QHBoxLayout()
        # self.combo = QComboBox()
        combo_layout.addWidget(self.combo, alignment=(Qt.AlignmentFlag.AlignCenter))
        self.combo.setFixedSize(500,40)
        self.combo.setStyleSheet("background-color:#e5c185; font-size: 18px;font-weight:700;border:2px solid #000;")



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
        self.Recording = QLabel("Stopped")
        self.Recording.setFixedSize(150,30)
        self.Recording.setStyleSheet(" background-color: #f50538; font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px; ")
        self.Recording_label = QLabel("Recording?")
        self.Recording_label.setFixedSize(150,30)
        self.Recording_label.setStyleSheet("font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px; ")
        self.label = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel("WPM")
        self.label4 = QLabel("Delay Rate")
        self.label3.setStyleSheet(" font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px; ")
        self.label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Recording.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Recording_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label3.setFixedSize(150,30)
        self.label4.setFixedSize(150,30)
        self.label4.setStyleSheet(" font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px;")
        label_layout2.addWidget(self.Recording_label)
        label_layout2.addWidget(self.label3)
        label_layout2.addWidget(self.label4)
        self.label.setFixedSize(150,30)
        self.label.setStyleSheet("background-color: #fdffb6; font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px;")
        label_layout.addWidget(self.Recording)
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
        self.speed_slider.valueChanged.connect(lambda value: self.send_speed(value))
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
        self.Receive = QPushButton("Start Recording")
        self.Receive.clicked.connect(self.toggle_recording)
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
        self.rx = QTextEdit()
        self.rx.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.rx.setStyleSheet("background-color: lightblue;font-size: 20px; font-weight: 700;")
        self.rx.setPlaceholderText("This is where you Press 'Receive Button' and receive converted Morse Code")
        self.rx.setFixedHeight(250)
        rx_layout.addWidget(self.rx)

        layout.addLayout(title_layout)
        layout.addLayout(combo_layout)
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

    def start_recording(self):
        self.recorder_thread = RecorderThread("output.wav")
        self.recorder_thread.start()

    def stop_recording(self):
        if self.recorder_thread:
            self.recorder_thread.stop()
            self.recorder_thread.wait()
            self.start_button.setEnabled(True)
            self.stop_button.setEnabled(False)
    
    def toggle_recording(self):
        if self.recorder_thread:
            # Stop recording
            self.recorder_thread.stop()
            self.recorder_thread.wait()
            self.Receive.setText("Start Recording")
            self.Recording.setStyleSheet("background-color: #e12729; font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px;")
            self.Recording.setText("Stopped")
            # self.timer.stop()
           
        else:
            # Start recording
            self.recorder_thread = RecorderThread("output.wav")
            self.recorder_thread.start()
            self.Receive.setText("Stop Recording")
            self.Recording.setStyleSheet("background-color: #72b043; font-size: 18px; font-weight: 700; font-family: 'Arial';border: 2px solid #000; border-radius: 15px;")
            self.Recording.setText("Recording")
            # self.timer.start(1000)  # Simulate recording every second
            print("Recording started.")

    def update_text_edit(self, text):
        # Update the QTextEdit with the selected text from the QComboBox
        self.snd.setText(text)


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

    def send_speed(self, value):
        value = self.speed_slider.value()
        command = f"@{value}\n"
        self.arduino.write(command.encode())


    def send_text(self):
        text = self.snd.text()
        message = f"{text}\n"
        self.arduino.write(str(message).encode())

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
