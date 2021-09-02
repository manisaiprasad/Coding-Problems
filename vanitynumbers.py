#!/bin/python3

import math
import os
import random
import re
import sys
#
# Complete the 'vanity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING_ARRAY numbers
#


def decode(code):
    keypad_map = {"A": 2, "B": 2, "C": 2, "D": 3, "E": 3, "F": 3, "G": 4, "H": 4, "I": 4, "J": 5, "K": 5, "L": 5,
                  "M": 6, "N": 6, "O": 6, "P": 7, "Q": 7, "R": 7, "S": 7, "T": 8, "U": 8, "V": 8, "W": 9, "X": 9, "Y": 9, "Z": 9}
    result = []
    for char in code:
        result.append(str(keypad_map[char]))
    # print(result)
    return "".join(result)


def vanity(codes, numbers):
    # Write your code here
    codes_to_numbers = []
    for code in codes:
        codes_to_numbers.append(decode(str(code)))
    result_numbers = []
    for number in numbers:
        for code_num in codes_to_numbers:
            if code_num in number and len(number) >= 11:
                result_numbers.append(number)
    result_set = set(result_numbers)
    result = list(result_set)
    result.sort()
    return result
