import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout,
    QListWidget, QListWidgetItem, QVBoxLayout
)

class RowWidget(QWidget):
    def __init__(self, row_data, parent=None):
        super().__init__(parent)
        self.row_data = row_data

        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(8)

        self.callsign_label = QLabel(row_data.get("callsign", "—"), self)
        self.name_label = QLabel(row_data.get("name", "—"), self)

        layout.addWidget(self.callsign_label)
        layout.addWidget(self.name_label)
        layout.addStretch(1)

        self.setLayout(layout)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QListWidget RowWidget test")
        self.list = QListWidget()

        v = QVBoxLayout(self)
        v.addWidget(self.list)
        self.setLayout(v)

        rows = [
            {"callsign": "K3XYZ", "name": "Alex"},
            {"callsign": "N2ABC", "name": "Riley"},
        ]
        for r in rows:
            w = RowWidget(r)
            item = QListWidgetItem()
            item.setSizeHint(w.sizeHint())  # ensure non-zero row height
            self.list.addItem(item)
            self.list.setItemWidget(item, w)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.resize(360, 200)
    win.show()
    sys.exit(app.exec())
