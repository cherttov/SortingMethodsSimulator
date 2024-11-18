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
        self.pushButton.clicked.connect(lambda: self.run_simulation(self.sample_size))
    
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
    def run_simulation(self, amount: int):
        chosen_sort = self.comboBox.currentText()
        start_time = time.time()

        sort = sorting_methods.get(chosen_sort, None)
        if sort is not None:
            sort() # WILL RETURN NUMBER OF ITERATIONS AS WELL!
        else:
            print("An error has occured: Sorting method not found.")

        elapsed_time = time.time() - start_time
        self.time_var.setText(f"TIME: {elapsed_time:.4f}s")
        self.sample_var.setText(f"SAMPLE SIZE: {amount}")
        self.iterations_var.setText(f"ITERATIONS: {None}")
    
    # Generates Lines Representing The Data We Generated
    def lines_generator(self) -> None:
        pass


if __name__=="__main__":
    app = QApplication([])
    main = SortingApp()
    main.show()
    app.exec()