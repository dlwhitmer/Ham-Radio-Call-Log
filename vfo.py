import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class VFO(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VFO")
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self._is_dragging = False
        self._drag_start_position = QPoint()
        self.setGeometry(300,100,700,400)
        self.setFixedSize(700,400)
        self.setStyleSheet("""
            QMainWindow {
                background-image: url('brushednickel-1.jpg');
                background-repeat: no-repeat;
                background-position: center;
                background-attachment: cover;
                           
            }
        """)

        title_layout = QHBoxLayout()
        self.title = QLabel("Amateur Radio VFO")
        title_layout.addWidget(self.title,alignment=(Qt.AlignmentFlag.AlignCenter))
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setFixedSize(300,40)
        self.title.setStyleSheet("background-color:#00aaff; font-size:30px; font-weight: 600; border:2px solid #000; border-radius: 15px;")

        exit_layout = QHBoxLayout()
        self.exit_btn = QPushButton("Exit")
        self.exit_btn.clicked.connect(self.exit_program)
        self.exit_btn.setFixedSize(100,30)
        self.exit_btn.setStyleSheet("background-color: #00aaff;font-size:14px;font-weight: 600;")
        exit_layout.addWidget(self.exit_btn, alignment=(Qt.AlignmentFlag.AlignCenter))

        freq_input_layout = QHBoxLayout()
        self.freq_input = QLabel("88:88", self)
        font = QFont("Digital-7", 25, QFont.Weight.Bold)
        self.freq_input.setFont(font)
        self.freq_input.clearFocus()
        self.freq_input.setFixedSize(200,50)
        self.freq_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.freq_input.setStyleSheet("""
            QLabel {
                color: lime;
                background-color: black;
                border: 2px solid darkgreen;
                padding: 10px;
                text-shadow: 2px 2px 5px green;
            }
        """)
        freq_input_layout.addWidget(self.freq_input, alignment= (Qt.AlignmentFlag.AlignCenter))

        label_layout = QHBoxLayout()
        self.band_label = QLabel("Choose Band")
        self.band_label.setFixedSize(200,25)
        self.band_label.setStyleSheet("background-color: #00aaff;font-size:18px; font-weight: 600; border:2px solid #000; border-radius: 15px;")
        self.band_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_layout.addWidget(self.band_label, alignment=(Qt.AlignmentFlag.AlignCenter))

        btn_layout = QHBoxLayout()
        self.meter_btn80 = QPushButton("80m Band")
        self.meter_btn80.setFixedSize(150,30)
        self.meter_btn80.clicked.connect(lambda: self.set_band_range(3500, 4000))
        self.meter_btn80.setStyleSheet("background-color:#00aaff; font-family: 'Times New Roman'; font-size:20px; font-weight: 700; border:2px solid #000;")
        self.meter_btn40 = QPushButton("40m Band")
        self.meter_btn40.setFixedSize(150,30)
        self.meter_btn40.clicked.connect(lambda: self.set_band_range(7000, 7300))
        self.meter_btn40.setStyleSheet("background-color:#00aaff; font-family: 'Times New Roman'; font-size:20px; font-weight: 700; border:2px solid #000;")
        self.meter_btn20 = QPushButton("20m Band")
        self.meter_btn20.setFixedSize(150,30)
        self.meter_btn20.clicked.connect(lambda: self.set_band_range(14000, 14350))
        self.meter_btn20.setStyleSheet("background-color:#00aaff; font-family: 'Times New Roman'; font-size:20px; font-weight: 700; border:2px solid #000;")
        self.meter_btn15 = QPushButton("15m Band")
        self.meter_btn15.setFixedSize(150,30)
        self.meter_btn15.clicked.connect(lambda: self.set_band_range(21000, 21450))
        self.meter_btn15.setStyleSheet("background-color:#00aaff; font-family: 'Times New Roman'; font-size:20px; font-weight: 700; border:2px solid #000;")
        self.meter_btn10 = QPushButton("10m Band")
        self.meter_btn10.setFixedSize(150,30)
        self.meter_btn10.clicked.connect(lambda: self.set_band_range(28000, 29700))
        self.meter_btn10.setStyleSheet("background-color:#00aaff; font-family: 'Times New Roman'; font-size:20px; font-weight: 700; border:2px solid #000;")
        btn_layout.addWidget(self.meter_btn80)
        btn_layout.addWidget(self.meter_btn40)
        btn_layout.addWidget(self.meter_btn20)
        btn_layout.addWidget(self.meter_btn15)
        btn_layout.addWidget(self.meter_btn10)


        
        tuning_slider_layout = QHBoxLayout()
        self.tune_slider = QSlider(Qt.Orientation.Horizontal, self)
        # self.tune_slider.setStyleSheet("background-color: #fff;")
        self.tune_slider.setFixedSize(500,40)
        self.tune_slider.setTickPosition(QSlider.TickPosition.TicksBelow)  # Show notches below the slider
        self.tune_slider.setMinimum(0)
        self.tune_slider.setMaximum(300)
        self.tune_slider.setValue(300)
        self.tune_slider.setSingleStep(1)
        self.tune_slider.valueChanged.connect(self.update_display)
        self.tune_slider.setStyleSheet("""
            QSlider::groove:horizontal {
                border: 1px solid #999;
                height: 8px;
                background: #b3b3b3;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #0078d7;
                border: 1px solid #5c5c5c;
                width: 30px;
                height: 10px;
                margin: -5px 0;  /* centers the handle vertically */
                border-radius: 0px;  /* removes rounded corners */
    }
            QSlider::handle:horizontal:hover {
                background: #ff784e;
            }
        """)
        tuning_slider_layout.addWidget(self.tune_slider)
        space_layout2 = QHBoxLayout()
        self.space2 = QLabel()
        self.space2.setFixedHeight(20)
        space_layout2.addWidget(self.space2)
        space_layout = QHBoxLayout()
        self.space = QLabel()
        self.space.setFixedHeight(20)
        space_layout.addWidget(self.space)

        layout.addLayout(title_layout)
        layout.addLayout(freq_input_layout)
        layout.addLayout(label_layout)
        layout.addLayout(btn_layout)
        layout.addLayout(space_layout)
        layout.addLayout(tuning_slider_layout)
        layout.addLayout(space_layout2)
        layout.addLayout(exit_layout)
       


    def update_display(self,value):
        mhz = value / 1000  # Convert kHz to MHz
        formatted = f"{mhz:.3f}"  # Format to 3 decimal places
        self.freq_input.setText(f"{formatted} MHz")

    def set_band_range(self, min_freq, max_freq):
        self.tune_slider.setMinimum(min_freq)
        self.tune_slider.setMaximum(max_freq)
        self.tune_slider.setValue(min_freq)  # Optional: reset to start of band

    def exit_program(self):
        """Exit the application."""
        QApplication.instance().quit()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._is_dragging = True
            self._drag_start_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._is_dragging and event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self._drag_start_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self._is_dragging = False
            event.accept()
        

app = QApplication([])
window = VFO()
window.show()
app.exec()