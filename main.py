import random
import time
from sorts import sorting_methods # SORTING
from design import Ui_MainWindow # DESIGN
from PyQt6.QtWidgets import QApplication, QMainWindow

class SortingApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Initializes GUI Variables and Variables
        super().__init__()
        self.setupUi(self)
        self.data = {}
        self.sample_size : int = 1 # changing this doesn't affect the code whatsoever
        self.delay_time : int = 0
        # Adds Pointer to Gui
        self.comboBox.addItems(sorting_methods)
        self.randomizeButton.clicked.connect(lambda: self.randomize_data(self.sample_size))
        self.pushButton.clicked.connect(lambda: self.run_simulation(self.sample_size))
        # Connects Amount Slider With Sample Var
        self.sample_var.setText(f"SAMPLE SIZE: {self.sample_size}")
        self.amount_slider.valueChanged.connect(self.update_sample_var)
        # Connects Delay Slider With Delay Var
        self.delay_var.setText(f"DELAY: {self.delay_time}ms")
        self.delay_slider.valueChanged.connect(self.update_delay_var)

    
    # Generates Dictionary With Unique Values For Each Key
    def data_generator(self, amount: int) -> dict[int, int]:
        data = {}
        for i in range(0, amount):
            value = random.randint(1, amount)
            # Randomizes Again If Value Exists In Dictionary
            while value in data.values():
                value = random.randint(1, amount)
            data[i] = value
        return data
    
    # Passes Randomized Data Dict to Data Variable
    def randomize_data(self, amount: int) -> None:
        self.data = self.data_generator(amount)
    
    # Matches Sorting Method and Runs It
    def run_simulation(self, amount: int) -> None:
        if len(self.data) > 0:
            # Initiates Start Time & Checks What Option Is Chosen
            chosen_sort = self.comboBox.currentText()
            start_time = time.time()
            # Runs Selected Sort Function in sorts.py
            sort = sorting_methods.get(chosen_sort, None)
            data_copy = self.data.copy()
            if sort is not None:
                sorted_dict, iterations = sort(data_copy, self.delay_time)
                self.frame.set_data(sorted_dict)
            else:
                print("An error has occured: Sorting method not found.")
            # Calculates Final Time
            elapsed_time = time.time() - start_time
            # Calculates Loss Percentage
            loss_percentage = 100 - len(sorted_dict.keys()) / (len(self.data) / 100)
            # Outputs Info About The Run
            self.method_chosen.setText(f"{chosen_sort}")
            self.time_var.setText(f" TIME: {elapsed_time*1000:.3f}ms")
            self.iterations_var.setText(f"ITERATIONS: {iterations}")
            self.loss_var.setText(f"LOSS PERCENTAGE: {loss_percentage:.1f}%")
        else:
            print("Error: Data Are Empty") # <-- !!!
    
    # Update Sample Size Label On Slider Movement
    def update_sample_var(self, value: int):
        self.sample_size = value
        self.sample_var.setText(f"SAMPLE SIZE: {value}")

    # Update Delay Time Label On Slider Movement
    def update_delay_var(self, value: int):
        self.delay_time = value
        self.delay_var.setText(f"DELAY: {value}ms")
    
    # Generates Lines Representing The Data We Generated
    def lines_generator(self) -> None:
        # Would have to "yield" results after each iteration in sorts.py
        raise NotImplementedError


if __name__=="__main__":
    app = QApplication([])
    main = SortingApp()
    main.show()
    app.exec()