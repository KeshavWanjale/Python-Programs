'''
4. Power of 2
    a. Desc -> This program takes a command-line argument N and prints a table of the
    powers of 2 that are less than or equal to 2^N.
    b. I/P -> The Power Value N. Only works if 0 <= N < 31 since 2^31 overflows an int
    c. Logic -> repeat until i equals N.
    d. O/P -> Print the year is a Leap Year or not.
'''
number_entered = input("Enter a number: ")

number = number_entered.isdigit() and int(number_entered) or None

if number != None and number < 31:
    print(f"Powers of 2 that are less than or equal to 2^{number}:")
    for i in range(number + 1):
        power_of_2 = 2 ** i
        print(f"2^{i} = {power_of_2}")
else:
    print("Invalid input! Please enter a valid positive integer.(0>=number<31)")