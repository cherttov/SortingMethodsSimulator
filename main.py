import random
import time
from sorts import sorting_methods
from design import Ui_MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow

class SortingApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.sample_size = 480
        self.data = self.data_generator(self.sample_size)
        self.setupUi(self)

        self.comboBox.addItems(sorting_methods)
        self.pushButton.clicked.connect(self.run_simulation)
    
    # Generates Dictionary With Unique Values For Each Key
    def data_generator(self, amount: int) -> dict[int, int]:
        data = {}
        for i in range(0, amount):
            value = random.randint(0, amount - 1)
            while value in data.values():
                value = random.randint(0, amount - 1)
            data[i] = value
        return data
    # Matches Sorting Method and Runs It
    def run_simulation(self):
        sorting_method = self.comboBox.currentText()
        start_time = time.time()
        print(sorting_method, start_time) # DEBUG!
    
    # Generates Lines Representing The Data We Generated
    def lines_generator(self) -> None:
        pass


if __name__=="__main__":
    app = QApplication([])
    main = SortingApp()
    main.show()
    app.exec()