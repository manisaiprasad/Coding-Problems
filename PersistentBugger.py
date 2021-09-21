# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
def persistence(n, count=0):
    # your code
    print(n)
    if len(str(n)) == 1:
        return count
    tokens = str(n)
    mul_num = 1
    for char in tokens:
        mul_num *= int(char)
    return persistence(mul_num, count+1)
