from typing import Callable


def BubbleSort():
    pass

def SelectionSort():
    pass

def InsertionSort():
    pass


sorting_methods : dict[str, Callable[[], dict[int, int]]]= {
    "Bubble Sort" : BubbleSort,
    "Selection Sort" : SelectionSort,
    "Insertion Sort" : InsertionSort}
