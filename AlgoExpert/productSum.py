# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array, multiplier=1):
    # Write your code here.
    sum = 0
    for item in array:
        if type(item) == list:
            sum += productSum(item, multiplier + 1)
        else:
            sum += item
    return sum * multiplier
