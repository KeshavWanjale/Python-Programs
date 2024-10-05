'''
5. Harmonic Number
    a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N
    (http://users.encs.concordia.ca/~chvatal/notes/harmonic.html).
    b. I/P -> The Harmonic Value N. Ensure N != 0
    c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
    d. O/P -> Print the Nth Harmonic Value.
'''

number_entered = input("Enter a number: ")

number = (number_entered.isdigit()) and int(number_entered) or None

harmonic_number = float(0)
if number != None and number>0:
    for i in range(1,number+1):
        harmonic_number += 1/i
    print(f"The {number}th Harmonic Value is {harmonic_number}.")
else:
    print(f"Invalid input: {number_entered}. Number must be greater than 0")