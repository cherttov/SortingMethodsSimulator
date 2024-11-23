from typing import Callable, Tuple
import asyncio


def BubbleSort(arr):
    iterations = 0
    for n in range(len(arr) - 1, 0, -1): 
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        iterations += 1
    return arr, iterations

def SelectionSort(arr):
    iterations = 0
    return arr, iterations

def InsertionSort(arr):
    iterations = 0
    return arr, iterations


sorting_methods : dict[str, Callable[[], Tuple[dict[int, int], int]]]= {
    "Bubble Sort" : BubbleSort,
    "Selection Sort" : SelectionSort,
    "Insertion Sort" : InsertionSort}
