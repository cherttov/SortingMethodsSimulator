from typing import Callable, Tuple
import asyncio


def BubbleSort(arr) -> Tuple[dict[int, int], int]:
    iterations = 0
    for n in range(len(arr) - 1, 0, -1): 
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        iterations += 1
    return arr, iterations

def SelectionSort(arr) -> Tuple[dict[int, int], int]:
    iterations = 0
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        iterations += 1
    return arr, iterations

def InsertionSort(arr) -> Tuple[dict[int, int], int]:
    iterations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        iterations += 1
    return arr, iterations

def Unsorted(arr) -> Tuple[dict[int, int], int]:
    iterations = 0
    return arr, iterations


sorting_methods : dict[str, Callable[[], Tuple[dict[int, int], int]]]= {
    "Bubble Sort" : BubbleSort,
    "Selection Sort" : SelectionSort,
    "Insertion Sort" : InsertionSort,
    "Unsorted" : Unsorted
    }
