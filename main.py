import random
import time
from sorts import sorting_methods # SORTING
from design import Ui_MainWindow # DESIGN
from PyQt6.QtWidgets import QApplication, QMainWindow
import threading


class SortingApp(QMainWindow, Ui_MainWindow):
    # Constructor
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
            # Checks What Option Is Chosen
            chosen_sort = self.comboBox.currentText()
            self.method_chosen.setText(f"{chosen_sort}")
            # Selects Chosen Sorting Function & Copies Data
            sort = sorting_methods.get(chosen_sort, None)
            data_copy = self.data.copy()
            # Runs The Sorting Simulation
            if sort is not None:
                # Initiates Start Time
                start_time = time.time()
                # Sorting Process & Visuals Updating
                thread = threading.Thread(target=self.update_sorting, args=(sort, data_copy, start_time))
                thread.start()
                #self.update_sorting(sort, data_copy, start_time)
            else:
                print("An error has occured: Sorting method not found.")
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
    def update_sorting(self, sort, data, start_time) -> None:
        # Have to break sorting function on simulation button call
        # Have to speed up visualisation (maybe by frequency update)
        # Have to fix not working sorts
        # I might need to add a 2nd thread to do some of this stuff

        # Run Sorting Simulation & Update Iterations/Elapsed Time Var
        for sorted_dict, iterations in sort(data, self.delay_time):
            # Update Frame Painter
            self.frame.set_data(sorted_dict)
            QApplication.processEvents()
            # Updates Iterations
            self.iterations_var.setText(f"ITERATIONS: {iterations}")
            # Calculates Final Time
            elapsed_time = time.time() - start_time
            self.time_var.setText(f" TIME: {elapsed_time*1000:.3f}ms")
        # Output Final Frame Paint
        self.frame.set_data(sorted_dict)
        # Calculates & Displays Loss Percentage
        loss_percentage = 100 - len(sorted_dict.keys()) / (len(self.data) / 100)
        self.loss_var.setText(f"LOSS PERCENTAGE: {loss_percentage:.1f}%")


if __name__=="__main__":
    app = QApplication([])
    main = SortingApp()
    main.show()
    app.exec()