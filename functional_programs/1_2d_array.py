'''
1. 2D Array
    a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
    standard input and printing them out to standard output.
    b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
    c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
    d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
    OutputStreamWriter to print the output to the screen.
'''

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    # we will create row list to store elements in each row
    row_list = []
    for j in range(columns):
        row_list.append(int(input("Enter number for 2d array: ")))
    # we will append the row list to matrix
    matrix.append(row_list)

# printing th 2d matrix
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=" ")
    print()
# print(matrix[1][1])