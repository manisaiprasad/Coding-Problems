# Consider a m x n matrix of characters inmatrix. Identify and print a m x n binary matrix outmatrix based on the below logic:
# idenitfy the unique characters in inmatirx

# Input format:
# First line will contain number of rows m of inmatrix.
# The next m lines will contain the elements of inmatrix. Each line will
# have n elements separated by *»(comma).
# Read the input from standard input stream,
# Output format:
# Print each row of the outmatrix in a new line where row elements are
# separated by % (comma)
# Print the output to the standard output stream
# Sample Input:
# 3
# a b c A
# a f c f
# a f c A
# Sample Output:
# 1,0,1,0
# 0,0,0,0
# 1,1,0,1

def input_matrix():
    m = int(input())
    inmatrix = []
    for i in range(m):
        inmatrix.append(input().split())
    return inmatrix

# For each unique character in in matrix
  # If the character is present in all rows of inmatrix, set 0 across all the positions where the character is occurring in out matrix
  # If the character is not present in all rows of inmatrix, but present in more than half of the rows, set 0 across all those positions where character is occurring at even rows of inmatrix and set 1 across all those positions where character is occurring at odd rows of inmatrix
  # If the character is present in at most half of the rows of inmatrix, set 1 across all the positions where the character is occurring in outmatrix
def find_unique_characters(inmatrix):
  unique_characters = []
  for row in inmatrix:
    for char in row:
      if char not in unique_characters:
        unique_characters.append(char)
  return unique_characters

# After all positions in outmatrix are set with 0s and 1s based on each unique characters' position, change their positions as below,
  # If there are equal number of 0s and 1s in a row of outmatrix, place them alternatively starting with 1 as the left-most element
  # If there are unequal number of 0s and 1s in a row of outmatrix, place the 1s edually at the both ends/left and right) and 0's in between. If there are odd number of 1s, the extra 1 would be placed along with 1s at the left end
  # If there are only 0s or only 1s in a row of outmatrix, retain them as-is

def set_outmatrix(inmatrix, unique_characters):
  outmatrix = [[0 for i in range(len(inmatrix[0]))] for j in range(len(inmatrix))]
  for char in unique_characters:
    count = 0
    for row in inmatrix:
      if char in row:
        count += 1
    if count == len(inmatrix):
      for i in range(len(inmatrix[0])):
        outmatrix[0][i] = 0
    elif count > len(inmatrix)//2:
      for i in range(len(inmatrix[0])):
        if i % 2 == 0:
          outmatrix[0][i] = 0
        else:
          outmatrix[0][i] = 1
    else:
      for i in range(len(inmatrix[0])):
        outmatrix[0][i] = 1
  return outmatrix


def printMatrix(outmatrix):
  for row in outmatrix:
    print(''.join(map(str, row)))

input_matrix = input_matrix()
unique_characters = find_unique_characters(input_matrix)
outmatrix = set_outmatrix(input_matrix, unique_characters)
printMatrix(outmatrix)


  
  

  
