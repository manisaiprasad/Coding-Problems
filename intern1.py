# All Ahmed is a mathematics professor who tries to involve his students in the class by conducting various fun activities. For today's session,
# he wanted to conduct a game for the students as follows:
# Given a set of integers with odd number of digits, the students should arrange them in ascending order based on the middle digit. If two
# numbers have same middle digit, display them in ascending order.
# Input
# First line consists of an integer 'n' representing the number of ID's to be verified followed by a second line with a set of 'n' integers that are
# single space separated
# Output
# Sorted list based on the middle digit
# Example:
# Input
# 5
# 10201 30215 90051 36103 92315

# Sorted list based on the middle digit
def solution(n, id_list):
    id_list = [int(i) for i in id_list.split()]
    id_list.sort(key=lambda x: str(x)[len(str(x))//2])
    for i in id_list:
        print(i)


n = int(input())
id_list = input()

solution(n, id_list)
