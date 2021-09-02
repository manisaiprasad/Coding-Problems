# you need to create a random array of size 100 (numbers of array should be between 0-10).
# You need to sort this array according to the frequency of occurance of each number.
# You are free to choose any sorting algorithm.

import random
import time

# Implementing Quick sort


def quickSort(array):
    # copying array to use same array for other sorting algorithms
    sorted_array = array.copy()

    # storing start time in begin
    begin = time.time()

    # performing sort using quickSortHelper function by passing the List, Starting index and Ending index
    quickSortHelper(sorted_array, 0, len(sorted_array)-1)

    # storing end time in end
    end = time.time()
    # finding total time
    total_time = end - begin

    # retuning the sorted array and time taken
    return sorted_array, total_time

# This Implementation takes last element as pivot, places the pivot element at its correct position in sorted array


def partition(arr, low, high):
    i = (low-1)    # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

# The helper function that implements QuickSort
# low is Starting index and high is Ending index


def quickSortHelper(arr, low, high):
    if low < high:

        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quickSortHelper(arr, low, pi-1)
        quickSortHelper(arr, pi+1, high)


# creating a random array of size 100 with numbers between 0-10
array = [random.randint(1, 10) for i in range(100)]
print(array)

# implementing the sort according to the frequency of occurance of each number


def sortByFrequency(sorted_array):
    frequency = {}

    # Performing this intial sort by value so that if any values are of equal frequency it will be sorted by value
    # Using the quickSort algorithm that we have implemented above
    sortedByValue, res_time = quickSort(array)

    # for each array element, insert into the dictionary and count its frequency
    for number in sortedByValue:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1
    print('frequency: ', frequency)

    # create a dictionary with frequency as key and numbers as the values
    # use lists in dictionary values to store multiple number which can have same frequency
    # keys become values and values becomes keys from frequency dictionary
    frequencyAsKey = {}
    for key, value in frequency.items():
        if value in frequencyAsKey:
            frequencyAsKey[value].append(key)
        else:
            frequencyAsKey[value] = [key]
    print("frequencyAsKey: ", frequencyAsKey, end="\n\n")

    # get all keys
    keys = list(frequencyAsKey.keys())
    # Using the quickSort algorithm that we have implemented above to sort the keys. keys the frequency
    keys_sorted, res_time = quickSort(keys)
    # reverse the array so it takes the higest frequency first
    sortedFrequencyKeys = keys_sorted[::-1]

    # building the sorted by frequency array from the sorted keys
    sortedByFrequency = []
    for key in sortedFrequencyKeys:
        numbers = frequencyAsKey[key]
        for number in numbers:
            for time in range(key):
                sortedByFrequency.append(number)
    # returning the final sort By Frequency array
    return sortedByFrequency


print("Input Array: ", array,  end="\n\n")
print("Output Array: ", sortByFrequency(array))
