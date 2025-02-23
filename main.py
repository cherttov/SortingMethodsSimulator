import random
import time
from sorts import sorting_methods # SORTING
from design import Ui_MainWindow # DESIGN
from PyQt6.QtWidgets import QApplication, QMainWindow

class SortingApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Initializes GUI Variables and Variables
        super().__init__()
        self.sample_size = 480 # 480
        self.data = {}
        self.setupUi(self)

        # Little To Do List
        # self.implement_this()

        # Adds Pointer to Gui
        self.comboBox.addItems(sorting_methods)
        self.randomizeButton.clicked.connect(self.randomize_data)
        self.pushButton.clicked.connect(lambda: self.run_simulation(self.sample_size))
    
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
    def randomize_data(self) -> None:
        self.data = self.data_generator(self.sample_size)
    
    # Matches Sorting Method and Runs It
    def run_simulation(self, amount: int) -> None:
        # Initiates Start Time & Checks What Option Is Chosen
        chosen_sort = self.comboBox.currentText()
        start_time = time.time()

        # Runs Selected Sort Function in sorts.py
        sort = sorting_methods.get(chosen_sort, None)
        data_copy = self.data.copy()
        if sort is not None:
            sorted_dict, iterations = sort(data_copy)
            self.frame.set_data(sorted_dict)
        else:
            print("An error has occured: Sorting method not found.")
        # Calculates Final Time
        elapsed_time = time.time() - start_time

        # Calculates Loss Percentage
        loss_percentage = 100 - len(sorted_dict.keys()) / (amount / 100)

        # Outputs Info About The Run
        self.method_chosen.setText(f"{chosen_sort}")
        self.time_var.setText(f"TIME: {elapsed_time*1000:.3f}ms")
        self.sample_var.setText(f"SAMPLE SIZE: {amount}")
        self.iterations_var.setText(f"ITERATIONS: {iterations}")
        self.loss_var.setText(f"LOSS PERCENTAGE: {loss_percentage:.1f}%")
    
    # Generates Lines Representing The Data We Generated
    def lines_generator(self) -> None:
        # Would have to "yield" results after each iteration in sorts.py
        raise NotImplementedError
    
    def implement_this(self) -> None:
        print("\n1. Add logs panel: for better debugging and for users to see what's going on")
        print("2. Add settings panel: for users to chose in what units to measure time, what sample size to use, etc.")
        print("3. Fix a bug where with sample size of e.g. 10, amount of objects shown on screen is 9")
        print("4. Add live visualisation of how the lines are rearranged in each sorting method")
        print("5. Add comments and explanations to VisualFrame in design.py")
        print("6. Add QuickSort & MergeSort")
        print("7. Add Loss percentage indicator: to see how much data have been lost")
        print("8. I don't think that iterations count is accurate, so check that")
        print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^CHECK THAT^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        input()


if __name__=="__main__":
    app = QApplication([])
    main = SortingApp()
    main.show()
    app.exec()