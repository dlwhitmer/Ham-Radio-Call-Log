
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *

class Sound_Recorder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("24 Track Sound Recorder")
        self.setGeometry(0,30,1920,750)
        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        title_layout = QHBoxLayout()
        self.title =QLabel("24 Track Studio")
        # self.title.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        title_layout.addWidget(self.title, alignment=(Qt.AlignmentFlag.AlignCenter))

        label_layout = QHBoxLayout()
        label_layout.setSpacing(5)  # or a small value like 5
        label_layout.setContentsMargins(0, 0, 0, 0)
        self.tr1_label = QLabel("Track 1")
        self.tr2_label = QLabel("Track 2")
        self.tr3_label = QLabel("Track 3")
        self.tr4_label = QLabel("Track 4")
        self.tr5_label = QLabel("Track 5")
        self.tr6_label = QLabel("Track 6")
        self.tr7_label = QLabel("Track 7")
        self.tr8_label = QLabel("Track 8")
        self.tr9_label = QLabel("Track 9")
        self.tr10_label = QLabel("Track 10")
        self.tr11_label = QLabel("Track 11")
        self.tr12_label = QLabel("Track 12")
        self.tr13_label = QLabel("Track 13")
        self.tr14_label = QLabel("Track 14")
        self.tr15_label = QLabel("Track 15")
        self.tr16_label = QLabel("Track 16")
        self.tr17_label = QLabel("Track 17")
        self.tr18_label = QLabel("Track 18")
        self.tr19_label = QLabel("Track 19")
        self.tr20_label = QLabel("Track 20")
        self.tr21_label = QLabel("Track 21")
        self.tr22_label = QLabel("Track 22")
        self.tr23_label = QLabel("Track 23")
        self.tr24_label = QLabel("Track 24")
        
        label_layout.addWidget(self.tr1_label)
        label_layout.addWidget(self.tr2_label)
        label_layout.addWidget(self.tr3_label)
        label_layout.addWidget(self.tr4_label)
        label_layout.addWidget(self.tr5_label)
        label_layout.addWidget(self.tr6_label)
        label_layout.addWidget(self.tr7_label)
        label_layout.addWidget(self.tr8_label)
        label_layout.addWidget(self.tr9_label)
        label_layout.addWidget(self.tr10_label)
        label_layout.addWidget(self.tr11_label)
        label_layout.addWidget(self.tr12_label)
        label_layout.addWidget(self.tr13_label)
        label_layout.addWidget(self.tr14_label)
        label_layout.addWidget(self.tr15_label)
        label_layout.addWidget(self.tr16_label)
        label_layout.addWidget(self.tr17_label)
        label_layout.addWidget(self.tr18_label)
        label_layout.addWidget(self.tr19_label)
        label_layout.addWidget(self.tr20_label)
        label_layout.addWidget(self.tr21_label)
        label_layout.addWidget(self.tr22_label)
        label_layout.addWidget(self.tr23_label)
        label_layout.addWidget(self.tr24_label)

        track_layout = QHBoxLayout()
        track_layout.setContentsMargins(0, 0, 0, 0)
        self.tr1 = QFrame()
        self.tr1.setFixedHeight(300)
        self.tr2 = QFrame()
        self.tr3 = QFrame()
        self.tr4 = QFrame()
        self.tr5 = QFrame()
        self.tr6 = QFrame()
        self.tr7 = QFrame()
        self.tr8 = QFrame()
        self.tr9 = QFrame()
        self.tr10 = QFrame()
        self.tr11 = QFrame()
        self.tr12 = QFrame()
        self.tr13 = QFrame()
        self.tr14 = QFrame()
        self.tr15 = QFrame()
        self.tr16 = QFrame()
        self.tr17 = QFrame()
        self.tr18 = QFrame()
        self.tr19 = QFrame()
        self.tr20 = QFrame()
        self.tr21 = QFrame()
        self.tr22 = QFrame()
        self.tr23 = QFrame()
        self.tr24 = QFrame()

        self.tr1.setStyleSheet("border: 1px solid #000;")
        self.tr2.setStyleSheet("border: 1px solid #000;")
        self.tr3.setStyleSheet("border: 1px solid #000;")
        self.tr4.setStyleSheet("border: 1px solid #000;")
        self.tr5.setStyleSheet("border: 1px solid #000;")
        self.tr6.setStyleSheet("border: 1px solid #000;")
        self.tr7.setStyleSheet("border: 1px solid #000;")
        self.tr8.setStyleSheet("border: 1px solid #000;")
        self.tr9.setStyleSheet("border: 1px solid #000;")
        self.tr10.setStyleSheet("border: 1px solid #000;")
        self.tr11.setStyleSheet("border: 1px solid #000;")
        self.tr12.setStyleSheet("border: 1px solid #000;")
        self.tr13.setStyleSheet("border: 1px solid #000;")
        self.tr14.setStyleSheet("border: 1px solid #000;")
        self.tr15.setStyleSheet("border: 1px solid #000;")
        self.tr16.setStyleSheet("border: 1px solid #000;")
        self.tr17.setStyleSheet("border: 1px solid #000;")
        self.tr18.setStyleSheet("border: 1px solid #000;")
        self.tr19.setStyleSheet("border: 1px solid #000;")
        self.tr20.setStyleSheet("border: 1px solid #000;")
        self.tr21.setStyleSheet("border: 1px solid #000;")
        self.tr22.setStyleSheet("border: 1px solid #000;")
        self.tr23.setStyleSheet("border: 1px solid #000;")
        self.tr24.setStyleSheet("border: 1px solid #000;")


        slider2_layout = QHBoxLayout()
        self.sltr1 = QFrame()
        self.sltr2 = QFrame()
        self.sltr3 = QFrame()
        self.sltr4 = QFrame()
        self.sltr5 = QFrame()
        self.sltr6 = QFrame()
        self.sltr7 = QFrame()
        self.sltr8 = QFrame()
        self.sltr9 = QFrame()
        self.sltr10 = QFrame()
        self.sltr11 = QFrame()
        self.sltr12 = QFrame()
        self.sltr13 = QFrame()
        self.sltr14 = QFrame()
        self.sltr15 = QFrame()
        self.sltr16 = QFrame()
        self.sltr17 = QFrame()
        self.sltr18 = QFrame()
        self.sltr19 = QFrame()
        self.sltr20 = QFrame()
        self.sltr21 = QFrame()
        self.sltr22 = QFrame()
        self.sltr23 = QFrame()
        self.sltr24 = QFrame()
        self.sltr25 = QFrame()
        self.sltr26 = QFrame()
        self.sltr27 = QFrame()
        self.sltr28 = QFrame()
        self.sltr29 = QFrame()
        self.sltr30 = QFrame()
        self.sltr31 = QFrame()
        self.sltr32 = QFrame()
        self.sltr33 = QFrame()
        self.sltr34 = QFrame()
        self.sltr35 = QFrame()
        self.sltr36 = QFrame()
        self.sltr37 = QFrame()
        self.sltr38 = QFrame()
        self.sltr39 = QFrame()
        self.sltr40 = QFrame()
        self.sltr41 = QFrame()
        self.sltr42 = QFrame()
        self.sltr43 = QFrame()
        self.sltr44 = QFrame()
        self.sltr45 = QFrame()
        self.sltr46 = QFrame()
        self.sltr47 = QFrame()
        self.sltr48 = QFrame()

        self.sltr1.setStyleSheet("border: 1px solid #000;")
        self.sltr2.setStyleSheet("border: 1px solid #000;")
        self.sltr3.setStyleSheet("border: 1px solid #000;")
        self.sltr4.setStyleSheet("border: 1px solid #000;")
        self.sltr5.setStyleSheet("border: 1px solid #000;")
        self.sltr6.setStyleSheet("border: 1px solid #000;")
        self.sltr7.setStyleSheet("border: 1px solid #000;")
        self.sltr8.setStyleSheet("border: 1px solid #000;")
        self.sltr9.setStyleSheet("border: 1px solid #000;")
        self.sltr10.setStyleSheet("border: 1px solid #000;")
        self.sltr11.setStyleSheet("border: 1px solid #000;")
        self.sltr12.setStyleSheet("border: 1px solid #000;")
        self.sltr13.setStyleSheet("border: 1px solid #000;")
        self.sltr14.setStyleSheet("border: 1px solid #000;")
        self.sltr15.setStyleSheet("border: 1px solid #000;")
        self.sltr16.setStyleSheet("border: 1px solid #000;")
        self.sltr17.setStyleSheet("border: 1px solid #000;")
        self.sltr18.setStyleSheet("border: 1px solid #000;")
        self.sltr19.setStyleSheet("border: 1px solid #000;")
        self.sltr20.setStyleSheet("border: 1px solid #000;")
        self.sltr21.setStyleSheet("border: 1px solid #000;")
        self.sltr22.setStyleSheet("border: 1px solid #000;")
        self.sltr23.setStyleSheet("border: 1px solid #000;")
        self.sltr24.setStyleSheet("border: 1px solid #000;")
        self.sltr25.setStyleSheet("border: 1px solid #000;")
        self.sltr26.setStyleSheet("border: 1px solid #000;")
        self.sltr27.setStyleSheet("border: 1px solid #000;")
        self.sltr28.setStyleSheet("border: 1px solid #000;")
        self.sltr29.setStyleSheet("border: 1px solid #000;")
        self.sltr30.setStyleSheet("border: 1px solid #000;")
        self.sltr31.setStyleSheet("border: 1px solid #000;")
        self.sltr32.setStyleSheet("border: 1px solid #000;")
        self.sltr33.setStyleSheet("border: 1px solid #000;")
        self.sltr34.setStyleSheet("border: 1px solid #000;")
        self.sltr35.setStyleSheet("border: 1px solid #000;")
        self.sltr36.setStyleSheet("border: 1px solid #000;")
        self.sltr37.setStyleSheet("border: 1px solid #000;")
        self.sltr38.setStyleSheet("border: 1px solid #000;")
        self.sltr39.setStyleSheet("border: 1px solid #000;")
        self.sltr40.setStyleSheet("border: 1px solid #000;")
        self.sltr41.setStyleSheet("border: 1px solid #000;")
        self.sltr42.setStyleSheet("border: 1px solid #000;")
        self.sltr43.setStyleSheet("border: 1px solid #000;")
        self.sltr44.setStyleSheet("border: 1px solid #000;")
        self.sltr45.setStyleSheet("border: 1px solid #000;")
        self.sltr46.setStyleSheet("border: 1px solid #000;")
        self.sltr47.setStyleSheet("border: 1px solid #000;")
        self.sltr48.setStyleSheet("border: 1px solid #000;")

        slider2_layout.addWidget(self.sltr1)
        slider2_layout.addWidget(self.sltr2)
        slider2_layout.addWidget(self.sltr3)
        slider2_layout.addWidget(self.sltr4)
        slider2_layout.addWidget(self.sltr5)
        slider2_layout.addWidget(self.sltr6)
        slider2_layout.addWidget(self.sltr7)
        slider2_layout.addWidget(self.sltr8)
        slider2_layout.addWidget(self.sltr9)
        slider2_layout.addWidget(self.sltr10)
        slider2_layout.addWidget(self.sltr11)
        slider2_layout.addWidget(self.sltr12)
        slider2_layout.addWidget(self.sltr13)
        slider2_layout.addWidget(self.sltr14)
        slider2_layout.addWidget(self.sltr15)
        slider2_layout.addWidget(self.sltr16)
        slider2_layout.addWidget(self.sltr17)
        slider2_layout.addWidget(self.sltr18)
        slider2_layout.addWidget(self.sltr19)
        slider2_layout.addWidget(self.sltr20)
        slider2_layout.addWidget(self.sltr21)
        slider2_layout.addWidget(self.sltr22)
        slider2_layout.addWidget(self.sltr23)
        slider2_layout.addWidget(self.sltr24)
        slider2_layout.addWidget(self.sltr25)
        slider2_layout.addWidget(self.sltr26)
        slider2_layout.addWidget(self.sltr27)
        slider2_layout.addWidget(self.sltr28)
        slider2_layout.addWidget(self.sltr29)
        slider2_layout.addWidget(self.sltr30)
        slider2_layout.addWidget(self.sltr31)
        slider2_layout.addWidget(self.sltr32)
        slider2_layout.addWidget(self.sltr33)
        slider2_layout.addWidget(self.sltr34)
        slider2_layout.addWidget(self.sltr35)
        slider2_layout.addWidget(self.sltr36)
        slider2_layout.addWidget(self.sltr37)
        slider2_layout.addWidget(self.sltr38)
        slider2_layout.addWidget(self.sltr39)
        slider2_layout.addWidget(self.sltr40)
        slider2_layout.addWidget(self.sltr41)
        slider2_layout.addWidget(self.sltr42)
        slider2_layout.addWidget(self.sltr43)
        slider2_layout.addWidget(self.sltr44)
        slider2_layout.addWidget(self.sltr45)
        slider2_layout.addWidget(self.sltr46)
        slider2_layout.addWidget(self.sltr47)
        slider2_layout.addWidget(self.sltr48)
       


        
        
        track_layout.addWidget(self.tr1)
        track_layout.addWidget(self.tr2)
        track_layout.addWidget(self.tr3)
        track_layout.addWidget(self.tr4)
        track_layout.addWidget(self.tr5)
        track_layout.addWidget(self.tr6)
        track_layout.addWidget(self.tr7)
        track_layout.addWidget(self.tr8)
        track_layout.addWidget(self.tr9)
        track_layout.addWidget(self.tr10)
        track_layout.addWidget(self.tr11)
        track_layout.addWidget(self.tr12)
        track_layout.addWidget(self.tr13)
        track_layout.addWidget(self.tr14)
        track_layout.addWidget(self.tr15)
        track_layout.addWidget(self.tr16)
        track_layout.addWidget(self.tr17)
        track_layout.addWidget(self.tr18)
        track_layout.addWidget(self.tr19)
        track_layout.addWidget(self.tr20)
        track_layout.addWidget(self.tr21)
        track_layout.addWidget(self.tr22)
        track_layout.addWidget(self.tr23)
        track_layout.addWidget(self.tr24)
        

        frame_layout1 = QVBoxLayout(self.sltr1)
        self.sltr1.setLayout(frame_layout1)
        frame_layout1.setContentsMargins(0, 0, 0, 0)
        self.vol = QProgressBar()
        self.vol.setFixedSize(23,221)
        self.vol.setOrientation(Qt.Orientation.Vertical)
        frame_layout1.addWidget(self.vol,alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)
        frame_layout2 = QVBoxLayout(self.sltr2)
        self.sltr2.setLayout(frame_layout2)
        frame_layout2.setContentsMargins(0, 0, 0, 0)
        self.slider = QSlider(Qt.Orientation.Vertical)
        self.slider.setFixedSize(22,221)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)  
        frame_layout2.addWidget(self.slider,alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        
        frame_layout3 = QVBoxLayout(self.sltr3)
        self.sltr3.setLayout(frame_layout3)
        frame_layout3.setContentsMargins(0, 0, 0, 0)
        self.vol2 = QProgressBar()
        self.vol2.setFixedSize(22, 221)
        self.vol2.setOrientation(Qt.Orientation.Vertical)
        frame_layout3.addWidget(self.vol2, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol2.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout4 = QVBoxLayout(self.sltr4)
        self.sltr4.setLayout(frame_layout4)
        frame_layout4.setContentsMargins(0, 0, 0, 0)
        self.slider2 = QSlider(Qt.Orientation.Vertical)
        self.slider2.setFixedSize(22,221)
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(100)
        self.slider2.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider2.setTickInterval(10)
        self.slider2.setSingleStep(1)  
        frame_layout4.addWidget(self.slider2,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout5 = QVBoxLayout(self.sltr5)
        self.sltr5.setLayout(frame_layout5)
        frame_layout5.setContentsMargins(0, 0, 0, 0)
        self.vol3 = QProgressBar()
        self.vol3.setFixedSize(22, 221)
        self.vol3.setOrientation(Qt.Orientation.Vertical)
        frame_layout5.addWidget(self.vol3, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol3.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout6 = QVBoxLayout(self.sltr6)
        self.sltr6.setLayout(frame_layout6)
        frame_layout6.setContentsMargins(0, 0, 0, 0)
        self.slider3 = QSlider(Qt.Orientation.Vertical)
        self.slider3.setFixedSize(22,221)
        self.slider3.setMinimum(0)
        self.slider3.setMaximum(100)
        self.slider3.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider3.setTickInterval(10)
        self.slider3.setSingleStep(1)  
        frame_layout6.addWidget(self.slider3,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout7 = QVBoxLayout(self.sltr7)
        self.sltr7.setLayout(frame_layout7)
        frame_layout7.setContentsMargins(0, 0, 0, 0)
        self.vol4 = QProgressBar()
        self.vol4.setFixedSize(22, 221)
        self.vol4.setOrientation(Qt.Orientation.Vertical)
        frame_layout7.addWidget(self.vol4, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol4.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout8 = QVBoxLayout(self.sltr8)
        self.sltr8.setLayout(frame_layout8)
        frame_layout8.setContentsMargins(0, 0, 0, 0)
        self.slider4 = QSlider(Qt.Orientation.Vertical)
        self.slider4.setFixedSize(22,221)
        self.slider4.setMinimum(0)
        self.slider4.setMaximum(100)
        self.slider4.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider4.setTickInterval(10)
        self.slider4.setSingleStep(1)  
        frame_layout8.addWidget(self.slider4,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout9 = QVBoxLayout(self.sltr9)
        self.sltr9.setLayout(frame_layout9)
        frame_layout9.setContentsMargins(0, 0, 0, 0)
        self.vol5 = QProgressBar()
        self.vol5.setFixedSize(22, 221)
        self.vol5.setOrientation(Qt.Orientation.Vertical)
        frame_layout9.addWidget(self.vol5, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol5.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout10 = QVBoxLayout(self.sltr10)
        self.sltr10.setLayout(frame_layout10)
        frame_layout10.setContentsMargins(0, 0, 0, 0)
        self.slider5 = QSlider(Qt.Orientation.Vertical)
        self.slider5.setFixedSize(22,221)
        self.slider5.setMinimum(0)
        self.slider5.setMaximum(100)
        self.slider5.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider5.setTickInterval(10)
        self.slider5.setSingleStep(1)  
        frame_layout10.addWidget(self.slider5,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout11 = QVBoxLayout(self.sltr11)
        self.sltr10.setLayout(frame_layout11)
        frame_layout11.setContentsMargins(0, 0, 0, 0)
        self.vol6 = QProgressBar()
        self.vol6.setFixedSize(22, 221)
        self.vol6.setOrientation(Qt.Orientation.Vertical)
        frame_layout11.addWidget(self.vol6, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol6.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout12 = QVBoxLayout(self.sltr12)
        self.sltr12.setLayout(frame_layout12)
        frame_layout12.setContentsMargins(0, 0, 0, 0)
        self.slider6 = QSlider(Qt.Orientation.Vertical)
        self.slider6.setFixedSize(22,221)
        self.slider6.setMinimum(0)
        self.slider6.setMaximum(100)
        self.slider6.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider6.setTickInterval(10)
        self.slider6.setSingleStep(1)  
        frame_layout12.addWidget(self.slider6,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout13 = QVBoxLayout(self.sltr13)
        self.sltr13.setLayout(frame_layout13)
        frame_layout13.setContentsMargins(0, 0, 0, 0)
        self.vol7 = QProgressBar()
        self.vol7.setFixedSize(22, 221)
        self.vol7.setOrientation(Qt.Orientation.Vertical)
        frame_layout13.addWidget(self.vol7, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol7.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout14 = QVBoxLayout(self.sltr14)
        self.sltr14.setLayout(frame_layout14)
        frame_layout14.setContentsMargins(0, 0, 0, 0)
        self.slider7 = QSlider(Qt.Orientation.Vertical)
        self.slider7.setFixedSize(22,221)
        self.slider7.setMinimum(0)
        self.slider7.setMaximum(100)
        self.slider7.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider7.setTickInterval(10)
        self.slider7.setSingleStep(1)  
        frame_layout14.addWidget(self.slider7,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))


        frame_layout15 = QVBoxLayout(self.sltr15)
        self.sltr15.setLayout(frame_layout15)
        frame_layout15.setContentsMargins(0, 0, 0, 0)
        self.vol8 = QProgressBar()
        self.vol8.setFixedSize(22, 221)
        self.vol8.setOrientation(Qt.Orientation.Vertical)
        frame_layout15.addWidget(self.vol8, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol8.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)     

        frame_layout16 = QVBoxLayout(self.sltr16)
        self.sltr16.setLayout(frame_layout16)
        frame_layout16.setContentsMargins(0, 0, 0, 0)
        self.slider8 = QSlider(Qt.Orientation.Vertical)
        self.slider8.setFixedSize(22,221)
        self.slider8.setMinimum(0)
        self.slider8.setMaximum(100)
        self.slider8.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider8.setTickInterval(10)
        self.slider8.setSingleStep(1)  
        frame_layout16.addWidget(self.slider8,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom)) 

        frame_layout17 = QVBoxLayout(self.sltr17)
        self.sltr16.setLayout(frame_layout17)
        frame_layout17.setContentsMargins(0, 0, 0, 0)
        self.vol9 = QProgressBar()
        self.vol9.setFixedSize(22, 221)
        self.vol9.setOrientation(Qt.Orientation.Vertical)
        frame_layout17.addWidget(self.vol9, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol9.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)  
        frame_layout18 = QVBoxLayout(self.sltr18)
        self.sltr16.setLayout(frame_layout18)
        frame_layout18.setContentsMargins(0, 0, 0, 0)
        self.slider9 = QSlider(Qt.Orientation.Vertical)
        self.slider9.setFixedSize(22,221)
        self.slider9.setMinimum(0)
        self.slider9.setMaximum(100)
        self.slider9.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider9.setTickInterval(10)
        self.slider9.setSingleStep(1)  
        frame_layout18.addWidget(self.slider9,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout19 = QVBoxLayout(self.sltr19)
        self.sltr19.setLayout(frame_layout19)
        frame_layout19.setContentsMargins(0, 0, 0, 0)
        self.vol10 = QProgressBar()
        self.vol10.setFixedSize(22, 221)
        self.vol10.setOrientation(Qt.Orientation.Vertical)
        frame_layout19.addWidget(self.vol10, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol10.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)

        frame_layout20 = QVBoxLayout(self.sltr20)
        self.sltr20.setLayout(frame_layout20)
        frame_layout20.setContentsMargins(0, 0, 0, 0)
        self.slider10 = QSlider(Qt.Orientation.Vertical)
        self.slider10.setFixedSize(22,221)
        self.slider10.setMinimum(0)
        self.slider10.setMaximum(100)
        self.slider10.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider10.setTickInterval(10)
        self.slider10.setSingleStep(1)  
        frame_layout20.addWidget(self.slider10,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout21 = QVBoxLayout(self.sltr21)
        self.sltr21.setLayout(frame_layout21)
        frame_layout21.setContentsMargins(0, 0, 0, 0)
        self.vol11 = QProgressBar()
        self.vol11.setFixedSize(22, 221)
        self.vol11.setOrientation(Qt.Orientation.Vertical)
        frame_layout21.addWidget(self.vol11, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol11.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)

        frame_layout22 = QVBoxLayout(self.sltr22)
        self.sltr22.setLayout(frame_layout22)
        frame_layout22.setContentsMargins(0, 0, 0, 0)
        self.slider11 = QSlider(Qt.Orientation.Vertical)
        self.slider11.setFixedSize(22,221)
        self.slider11.setMinimum(0)
        self.slider11.setMaximum(100)
        self.slider11.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider11.setTickInterval(10)
        self.slider11.setSingleStep(1)  
        frame_layout22.addWidget(self.slider11,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout23 = QVBoxLayout(self.sltr23)
        self.sltr23.setLayout(frame_layout23)
        frame_layout23.setContentsMargins(0, 0, 0, 0)
        self.vol12 = QProgressBar()
        self.vol12.setFixedSize(22, 221)
        self.vol12.setOrientation(Qt.Orientation.Vertical)
        frame_layout23.addWidget(self.vol12, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol12.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """) 

        frame_layout24 = QVBoxLayout(self.sltr24)
        self.sltr24.setLayout(frame_layout24)
        frame_layout24.setContentsMargins(0, 0, 0, 0)
        self.slider12 = QSlider(Qt.Orientation.Vertical)
        self.slider12.setFixedSize(22,221)
        self.slider12.setMinimum(0)
        self.slider12.setMaximum(100)
        self.slider12.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider12.setTickInterval(10)
        self.slider12.setSingleStep(1)  
        frame_layout24.addWidget(self.slider12,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout25 = QVBoxLayout(self.sltr25)
        self.sltr25.setLayout(frame_layout25)
        frame_layout25.setContentsMargins(0, 0, 0, 0)
        self.vol13 = QProgressBar()
        self.vol13.setFixedSize(22, 221)
        self.vol13.setOrientation(Qt.Orientation.Vertical)
        frame_layout25.addWidget(self.vol13, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol13.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout26 = QVBoxLayout(self.sltr26)
        self.sltr26.setLayout(frame_layout26)
        frame_layout26.setContentsMargins(0, 0, 0, 0)
        self.slider13 = QSlider(Qt.Orientation.Vertical)
        self.slider13.setFixedSize(22,221)
        self.slider13.setMinimum(0)
        self.slider13.setMaximum(100)
        self.slider13.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider13.setTickInterval(10)
        self.slider13.setSingleStep(1)  
        frame_layout26.addWidget(self.slider13,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout27 = QVBoxLayout(self.sltr27)
        self.sltr27.setLayout(frame_layout27)
        frame_layout27.setContentsMargins(0, 0, 0, 0)
        self.vol14 = QProgressBar()
        self.vol14.setFixedSize(22, 221)
        self.vol14.setOrientation(Qt.Orientation.Vertical)
        frame_layout27.addWidget(self.vol14, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol14.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout28 = QVBoxLayout(self.sltr28)
        self.sltr26.setLayout(frame_layout28)
        frame_layout28.setContentsMargins(0, 0, 0, 0)
        self.slider14 = QSlider(Qt.Orientation.Vertical)
        self.slider14.setFixedSize(22,221)
        self.slider14.setMinimum(0)
        self.slider14.setMaximum(100)
        self.slider14.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider14.setTickInterval(10)
        self.slider14.setSingleStep(1)  
        frame_layout28.addWidget(self.slider14,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout29 = QVBoxLayout(self.sltr29)
        self.sltr29.setLayout(frame_layout29)
        frame_layout29.setContentsMargins(0, 0, 0, 0)
        self.vol15 = QProgressBar()
        self.vol15.setFixedSize(22, 221)
        self.vol15.setOrientation(Qt.Orientation.Vertical)
        frame_layout29.addWidget(self.vol15, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol15.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout30 = QVBoxLayout(self.sltr30)
        self.sltr26.setLayout(frame_layout30)
        frame_layout30.setContentsMargins(0, 0, 0, 0)
        self.slider15 = QSlider(Qt.Orientation.Vertical)
        self.slider15.setFixedSize(22,221)
        self.slider15.setMinimum(0)
        self.slider15.setMaximum(100)
        self.slider15.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider15.setTickInterval(10)
        self.slider15.setSingleStep(1)  
        frame_layout30.addWidget(self.slider15,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout31 = QVBoxLayout(self.sltr31)
        self.sltr31.setLayout(frame_layout31)
        frame_layout31.setContentsMargins(0, 0, 0, 0)
        self.vol16 = QProgressBar()
        self.vol16.setFixedSize(22, 221)
        self.vol16.setOrientation(Qt.Orientation.Vertical)
        frame_layout31.addWidget(self.vol16, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol16.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout32 = QVBoxLayout(self.sltr32)
        self.sltr32.setLayout(frame_layout31)
        frame_layout32.setContentsMargins(0, 0, 0, 0)
        self.slider16 = QSlider(Qt.Orientation.Vertical)
        self.slider16.setFixedSize(22,221)
        self.slider16.setMinimum(0)
        self.slider16.setMaximum(100)
        self.slider16.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider16.setTickInterval(10)
        self.slider16.setSingleStep(1)  
        frame_layout32.addWidget(self.slider16,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout33 = QVBoxLayout(self.sltr33)
        self.sltr33.setLayout(frame_layout33)
        frame_layout33.setContentsMargins(0, 0, 0, 0)
        self.vol17 = QProgressBar()
        self.vol17.setFixedSize(22, 221)
        self.vol17.setOrientation(Qt.Orientation.Vertical)
        frame_layout33.addWidget(self.vol17, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol17.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout34 = QVBoxLayout(self.sltr34)
        self.sltr34.setLayout(frame_layout33)
        frame_layout34.setContentsMargins(0, 0, 0, 0)
        self.slider17 = QSlider(Qt.Orientation.Vertical)
        self.slider17.setFixedSize(22,221)
        self.slider17.setMinimum(0)
        self.slider17.setMaximum(100)
        self.slider17.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider17.setTickInterval(10)
        self.slider17.setSingleStep(1)  
        frame_layout34.addWidget(self.slider17,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout35 = QVBoxLayout(self.sltr35)
        self.sltr35.setLayout(frame_layout35)
        frame_layout35.setContentsMargins(0, 0, 0, 0)
        self.vol18 = QProgressBar()
        self.vol18.setFixedSize(22, 221)
        self.vol18.setOrientation(Qt.Orientation.Vertical)
        frame_layout35.addWidget(self.vol18, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol18.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout36 = QVBoxLayout(self.sltr36)
        self.sltr36.setLayout(frame_layout36)
        frame_layout36.setContentsMargins(0, 0, 0, 0)
        self.slider18 = QSlider(Qt.Orientation.Vertical)
        self.slider18.setFixedSize(22,221)
        self.slider18.setMinimum(0)
        self.slider18.setMaximum(100)
        self.slider18.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider18.setTickInterval(10)
        self.slider18.setSingleStep(1)  
        frame_layout36.addWidget(self.slider18,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout37 = QVBoxLayout(self.sltr37)
        self.sltr37.setLayout(frame_layout37)
        frame_layout37.setContentsMargins(0, 0, 0, 0)
        self.vol19 = QProgressBar()
        self.vol19.setFixedSize(22, 221)
        self.vol19.setOrientation(Qt.Orientation.Vertical)
        frame_layout37.addWidget(self.vol19, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol19.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout38 = QVBoxLayout(self.sltr38)
        self.sltr38.setLayout(frame_layout38)
        frame_layout38.setContentsMargins(0, 0, 0, 0)
        self.slider19 = QSlider(Qt.Orientation.Vertical)
        self.slider19.setFixedSize(22,221)
        self.slider19.setMinimum(0)
        self.slider19.setMaximum(100)
        self.slider19.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider19.setTickInterval(10)
        self.slider19.setSingleStep(1)  
        frame_layout38.addWidget(self.slider19,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout39 = QVBoxLayout(self.sltr39)
        self.sltr39.setLayout(frame_layout39)
        frame_layout39.setContentsMargins(0, 0, 0, 0)
        self.vol19 = QProgressBar()
        self.vol19.setFixedSize(22, 221)
        self.vol19.setOrientation(Qt.Orientation.Vertical)
        frame_layout39.addWidget(self.vol19, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol19.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout40 = QVBoxLayout(self.sltr40)
        self.sltr40.setLayout(frame_layout39)
        frame_layout40.setContentsMargins(0, 0, 0, 0)
        self.slider19 = QSlider(Qt.Orientation.Vertical)
        self.slider19.setFixedSize(22,221)
        self.slider19.setMinimum(0)
        self.slider19.setMaximum(100)
        self.slider19.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider19.setTickInterval(10)
        self.slider19.setSingleStep(1)  
        frame_layout40.addWidget(self.slider19,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout41 = QVBoxLayout(self.sltr41)
        self.sltr41.setLayout(frame_layout41)
        frame_layout41.setContentsMargins(0, 0, 0, 0)
        self.vol20 = QProgressBar()
        self.vol20.setFixedSize(22, 221)
        self.vol20.setOrientation(Qt.Orientation.Vertical)
        frame_layout41.addWidget(self.vol20, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol20.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout42 = QVBoxLayout(self.sltr42)
        self.sltr42.setLayout(frame_layout42)
        frame_layout42.setContentsMargins(0, 0, 0, 0)
        self.slider20 = QSlider(Qt.Orientation.Vertical)
        self.slider20.setFixedSize(22,221)
        self.slider20.setMinimum(0)
        self.slider20.setMaximum(100)
        self.slider20.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider20.setTickInterval(10)
        self.slider20.setSingleStep(1)  
        frame_layout42.addWidget(self.slider20,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout43 = QVBoxLayout(self.sltr43)
        self.sltr43.setLayout(frame_layout43)
        frame_layout43.setContentsMargins(0, 0, 0, 0)
        self.vol21 = QProgressBar()
        self.vol21.setFixedSize(22, 221)
        self.vol21.setOrientation(Qt.Orientation.Vertical)
        frame_layout43.addWidget(self.vol21, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol21.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout44 = QVBoxLayout(self.sltr44)
        self.sltr44.setLayout(frame_layout44)
        frame_layout44.setContentsMargins(0, 0, 0, 0)
        self.slider21 = QSlider(Qt.Orientation.Vertical)
        self.slider21.setFixedSize(22,221)
        self.slider21.setMinimum(0)
        self.slider21.setMaximum(100)
        self.slider21.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider21.setTickInterval(10)
        self.slider21.setSingleStep(1)  
        frame_layout44.addWidget(self.slider21,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout45 = QVBoxLayout(self.sltr45)
        self.sltr45.setLayout(frame_layout45)
        frame_layout45.setContentsMargins(0, 0, 0, 0)
        self.vol22 = QProgressBar()
        self.vol22.setFixedSize(22, 221)
        self.vol22.setOrientation(Qt.Orientation.Vertical)
        frame_layout45.addWidget(self.vol22, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol22.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout46 = QVBoxLayout(self.sltr46)
        self.sltr46.setLayout(frame_layout46)
        frame_layout46.setContentsMargins(0, 0, 0, 0)
        self.slider22 = QSlider(Qt.Orientation.Vertical)
        self.slider22.setFixedSize(22,221)
        self.slider22.setMinimum(0)
        self.slider22.setMaximum(100)
        self.slider22.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider22.setTickInterval(10)
        self.slider22.setSingleStep(1)  
        frame_layout46.addWidget(self.slider22,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))

        frame_layout47 = QVBoxLayout(self.sltr47)
        self.sltr47.setLayout(frame_layout47)
        frame_layout47.setContentsMargins(0, 0, 0, 0)
        self.vol23 = QProgressBar()
        self.vol23.setFixedSize(22, 221)
        self.vol23.setOrientation(Qt.Orientation.Vertical)
        frame_layout47.addWidget(self.vol23, alignment=(Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignBottom))
        self.vol23.setStyleSheet("""
        QProgressBar {
            padding: 0px;
            margin: 0px;
            border: 1px solid #000;
            background-color: transparent;
        }
        QProgressBar::chunk {
            background-color: #05B8CC;
            margin: 0px;
        }
        """)        
        
        frame_layout48 = QVBoxLayout(self.sltr48)
        self.sltr48.setLayout(frame_layout48)
        frame_layout48.setContentsMargins(0, 0, 0, 0)
        self.slider23 = QSlider(Qt.Orientation.Vertical)
        self.slider23.setFixedSize(22,221)
        self.slider23.setMinimum(0)
        self.slider23.setMaximum(100)
        self.slider23.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.slider23.setTickInterval(10)
        self.slider23.setSingleStep(1)  
        frame_layout48.addWidget(self.slider23,alignment=(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignBottom))



        
        layout.addLayout(title_layout)
        layout.addLayout(label_layout)
        layout.addLayout(track_layout)
        layout.addLayout(slider2_layout)


app = QApplication([])
window = Sound_Recorder()
window.show()
app.exec()