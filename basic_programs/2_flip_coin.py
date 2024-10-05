'''
2. Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads
c. O/P -> Percentage of Head vs Tails
'''
import random

number_of_flips_entered = input("Enter the number of times to Flip Coin: ")

number_of_flips = number_of_flips_entered.isdigit() and int(number_of_flips_entered) or None

heads = tails = 0

if number_of_flips != None:
    for i in range(number_of_flips):
        # random.random() selects a random float value between 0.0 to 1.0
        if random.random() > 0.5:
            heads += 1
        else:
            tails += 1
    heads_percentage = (heads / number_of_flips) * 100
    tails_percentage = (tails / number_of_flips) * 100

    print(f"Total flips: {number_of_flips}")
    print(f"Heads: {heads}, Percentage: {heads_percentage:.2f}%")
    print(f"Tails: {tails}, Percentage: {tails_percentage:.2f}%")
else:
    print(f"Invalid input {number_of_flips_entered}. Number must be greater than 0")