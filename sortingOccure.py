# you need to create a random array of size 100 (numbers of array should be between 0-10).
# You need to sort this array according to the frequency of occurance of each number.
# You are free to choose any sorting algorithm.

# creating a random array of size 100 with numbers between 0-10
import random
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
