# John Schmidt works as the data entry operator in New York. His daily activity includes assigning vehicle number for the new vehicles that
# enter the city. The vehicle number has the following format:
# First two letters represent the state
# Next one/two letter represent the series number (A to Z and AA to ZZ)
# Last 5 digits represent the Vehicle nurber
# When the vehicle number reached 99999, the next series will start from 00001. As there is a huge amount of vehicle movement now days,
# he wants to automate the process. Help john to auto generate 'n' vehicle numbers given the starting vehicle number.
# Input
# String representing the current vehicle number followed by Single integer representing value of 'n'
# Output
# n lines with number of car plates following the given number plate

def solution(v_num, n):
    state, series, number = v_num.split(' ')
    series_num = int(number)
    for i in range(n):
        series_num += 1
        if series_num > 99999:
            series_num = 1
            series = chr(ord(series) + 1)
        number = str(series_num).zfill(5)
        print(state+' ' + series+' ' + number)

n = int(input())
v_num = input()

solution(v_num, n)
