from typing import Callable, Tuple
import time


def BubbleSort(arr, delay) -> Tuple[dict[int, int], int]:
    iterations = 0
    for n in range(len(arr) - 1, 0, -1): 
        for i in range(n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        time.sleep(delay/1000)
        iterations += 1
    return arr, iterations


def SelectionSort(arr, delay) -> Tuple[dict[int, int], int]:
    iterations = 0
    for i in range(0, len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        time.sleep(delay/1000)
        iterations += 1
    return arr, iterations


def InsertionSort(arr, delay) -> Tuple[dict[int, int], int]:
    iterations = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        time.sleep(delay/1000)
        iterations += 1
    return arr, iterations


def QuickSort(arr, delay) -> Tuple[dict[int, int], int]:
    iterations = 0
    def partition(low, high):
        nonlocal iterations
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        time.sleep(delay/1000)
        iterations += 1
        return i + 1
    def quick_sort_recursive(low, high):
        nonlocal iterations
        if low < high:
            pivot_index = partition(low, high)
            iterations += 1
            quick_sort_recursive(low, pivot_index-1)
            quick_sort_recursive(pivot_index+1, high)
    quick_sort_recursive(0, len(arr)-1)
    return arr, iterations


def MergeSort(arr, delay) -> Tuple[dict[int, int], int]:
    iterations = 0
    raise NotImplementedError
    return arr, iterations


def StalinSort(arr, delay) -> Tuple[dict[int, int], int]:
    iterations = 0
    items = list(arr.items())
    sorted_items = [items[0]]
    for key, value in items[1:]:
        if value >= sorted_items[-1][1]:
            sorted_items.append((key, value))
        time.sleep(delay/1000)
        iterations += 1
    arr = dict(sorted_items)
    return arr, iterations


def Unsorted(arr, delay) -> Tuple[dict[int, int], int]:
    iterations = 0
    return arr, iterations


sorting_methods : dict[str, Callable[[], Tuple[dict[int, int], int]]]= {
    "Bubble Sort" : BubbleSort,
    "Selection Sort" : SelectionSort,
    "Insertion Sort" : InsertionSort,
    "Quick Sort" : QuickSort,
    "Merge Sort" : MergeSort,
    "Stalin Sort" : StalinSort,
    "Unsorted" : Unsorted
    }
