from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor

# idfk wtf is happening with the naming there, I am too lazy to fix that
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Window / Root
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("Sorting Method Simulator")
        self.centralWidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralWidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")

        # Font Settings
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)

        # Method Chosen Text
        self.method_chosen = QtWidgets.QLabel(parent=self.centralWidget)
        self.method_chosen.setFont(font)
        self.method_chosen.setObjectName("MethodChosen")
        self.gridLayout.addWidget(self.method_chosen, 0, 0, 1, 1)

        # Randomize Push Button
        self.randomizeButton = QtWidgets.QPushButton(parent=self.centralWidget)
        self.randomizeButton.setObjectName("randomizePushButton")
        self.gridLayout.addWidget(self.randomizeButton, 0, 2, 1, 1)

        # Methods Combo Box
        self.comboBox = QtWidgets.QComboBox(parent=self.centralWidget)
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
        self.frame = VisualFrame(parent=self.centralWidget)
        self.frame.setObjectName("visual_frame")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 4)

        # Updated Font Settings
        font = QtGui.QFont()
        font.setPointSize(10)

        # Delay Text
        self.delay_var = QtWidgets.QLabel(parent=self.centralWidget)
        self.delay_var.setFont(font)
        self.delay_var.setObjectName("delay_var")
        self.gridLayout.addWidget(self.delay_var, 2, 0, 1, 1)

        # Sample Size Text
        self.sample_var = QtWidgets.QLabel(parent=self.centralWidget)
        self.sample_var.setFont(font)
        self.sample_var.setObjectName("sample_var")
        self.gridLayout.addWidget(self.sample_var, 2, 1, 1, 1)

        # Iterations Count Text
        self.iterations_var = QtWidgets.QLabel(parent=self.centralWidget)
        self.iterations_var.setFont(font)
        self.iterations_var.setObjectName("label")
        self.gridLayout.addWidget(self.iterations_var, 2, 2, 1, 1)

        # Simulation Push Button
        self.pushButton = QtWidgets.QPushButton(parent=self.centralWidget)
        self.pushButton.setObjectName("simulatePushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 3, 1, 1)

        # Slider Size Policy
        slider_size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Ignored, QtWidgets.QSizePolicy.Policy.Fixed)

        # Size Slider
        self.amount_slider = QtWidgets.QSlider(parent=self.centralWidget)
        self.amount_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.amount_slider.setSizePolicy(slider_size_policy)
        self.amount_slider.setObjectName("amount_slider")
        self.amount_slider.setMinimum(1)
        self.amount_slider.setMaximum(4096)
        self.gridLayout.addWidget(self.amount_slider, 3, 1, 1, 1)
        
        # Delay Slider
        self.delay_slider = QtWidgets.QSlider(parent=self.centralWidget)
        self.delay_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.delay_slider.setSizePolicy(slider_size_policy)
        self.delay_slider.setObjectName("delay_slider")
        self.gridLayout.addWidget(self.delay_slider, 3, 0, 1, 1)

        # Loss Percentage Label
        self.loss_var = QtWidgets.QLabel(parent=self.centralWidget)
        self.loss_var.setFont(font)
        self.loss_var.setObjectName("loss_var")
        self.loss_var.setMaximumHeight(12)
        self.gridLayout.addWidget(self.loss_var, 3, 2, 1, 1)

        # Time Elapsed Text
        self.time_var = QtWidgets.QLabel(parent=self.centralWidget)
        self.time_var.setFont(font)
        self.time_var.setObjectName("time_var")
        self.gridLayout.addWidget(self.time_var, 3, 3, 1, 1)

        # Status Bar (not used for now)
        # self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        
        MainWindow.setCentralWidget(self.centralWidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.method_chosen.setText(_translate("MainWindow", "Sorting Method"))
        self.time_var.setText(_translate("MainWindow", " TIME:"))
        self.sample_var.setText(_translate("MainWindow", "SAMPLE SIZE:"))
        self.iterations_var.setText(_translate("MainWindow", "ITERATIONS:"))
        self.pushButton.setText(_translate("MainWindow", "SIMULATE"))
        self.randomizeButton.setText(_translate("MainWindow", "RANDOMIZE"))
        self.loss_var.setText(_translate("MainWindow", "LOSS PERCENTAGE:"))
        self.delay_var.setText(_translate("MainWindow", "DELAY:"))


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
