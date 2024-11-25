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
    return arr, iterations

def InsertionSort(arr) -> Tuple[dict[int, int], int]:
    iterations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # print(f"Pass {i}, key={key}, starting array: {arr}")  # --- DEBUG ---
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        iterations += 1
    return arr, iterations


sorting_methods : dict[str, Callable[[], Tuple[dict[int, int], int]]]= {
    "Bubble Sort" : BubbleSort,
    "Selection Sort" : SelectionSort,
    "Insertion Sort" : InsertionSort}
