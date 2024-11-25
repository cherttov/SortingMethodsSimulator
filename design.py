from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Window / Root
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("Sorting Method Simulator")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # Method Chosen Text
        self.MethodChosen = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        self.MethodChosen.setFont(font)
        self.MethodChosen.setObjectName("MethodChosen")
        self.gridLayout.addWidget(self.MethodChosen, 0, 0, 1, 1)

        # Methods Combo Box
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout.addWidget(self.comboBox, 0, 3, 1, 1)

        # Simulation Visual Frame
        # self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        # self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        # self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        # self.frame.setObjectName("visual_frame")
        # self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        # self.horizontalLayout.setObjectName("horizontalLayout")
        # self.gridLayout.addWidget(self.frame, 1, 0, 1, 4)
        self.frame = VisualFrame(parent=self.centralwidget)
        self.frame.setObjectName("visual_frame")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 4)

        # Time Elapsed Text
        self.time_var = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.time_var.setFont(font)
        self.time_var.setObjectName("time_var")
        self.gridLayout.addWidget(self.time_var, 2, 0, 1, 1)

        # Sample Size Text
        self.sample_var = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.sample_var.setFont(font)
        self.sample_var.setObjectName("sample_var")
        self.gridLayout.addWidget(self.sample_var, 2, 1, 1, 1)

        # Iterations Count Text
        self.iterations_var = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.iterations_var.setFont(font)
        self.iterations_var.setObjectName("label")
        self.gridLayout.addWidget(self.iterations_var, 2, 2, 1, 1)

        # Simulation Push Button
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.MethodChosen.setText(_translate("MainWindow", "Sorting Method"))
        self.time_var.setText(_translate("MainWindow", "TIME:"))
        self.sample_var.setText(_translate("MainWindow", "SAMPLE SIZE:"))
        self.iterations_var.setText(_translate("MainWindow", "ITERATIONS:"))
        self.pushButton.setText(_translate("MainWindow", "SIMULATE"))

class VisualFrame(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.data = {}
    
    def set_data(self, data):
        self.data = data
        self.update()

    def paintEvent(self, event):
        if not self.data:
            return
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        width = self.width()
        height = self.height()
        bar_width = width / len(self.data)

        for i, value in self.data.items():
            x = int(i * bar_width)
            line_height = int((value / max(self.data.values())) * height)
            painter.setPen(QColor("blue"))
            painter.drawLine(x, height, x, height - line_height)
        
        painter.end()
