'''
2. Sum of three Integer adds to ZERO
a. Desc -> A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.
b. I/P -> N number of integer, and N integer input array
c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
d. O/P -> One Output is number of distinct triplets as well as the second output is to
'''

def triplates_with_zero_sum(arr):
    n = len(arr)
    found = False
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    found = True
                    print(f"Triplets with zero sum are {arr[i]}, {arr[j]}, {arr[k]}")
    if(found == False):
        print("No triplets found whose sum is equal to zero.")   

triplates_with_zero_sum([10,-5,-5,-2,-8])