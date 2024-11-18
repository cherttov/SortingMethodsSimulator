from typing import Callable
import asyncio


def BubbleSort():
    return "Bubble Sort - works -"

def SelectionSort():
    return "Selection Sort - works -"

def InsertionSort():
    return "Insertion Sort - works -"


sorting_methods : dict[str, Callable[[], dict[int, int]]]= {
    "Bubble Sort" : BubbleSort,
    "Selection Sort" : SelectionSort,
    "Insertion Sort" : InsertionSort}
