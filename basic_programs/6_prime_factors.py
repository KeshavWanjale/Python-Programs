'''
6. Factors(Brute)
    a. Desc -> Computes the prime factorization of N using brute force.
    b. I/P -> Number to find the prime factors
    c. Logic -> Traverse till i*i <= N instead of i <= N for efficiency.
    d. O/P -> Print the prime factors of number N.
Prime Factors: A factor which is a prime number and not a composite number 
is a prime factor. For example, 2, 3 and 5 are the prime factors of 30.
'''

def get_prime_factors(number):
    prime_factors = []
    # if number is less than 2 return empty list
    if(number) < 2:
        return prime_factors
    
    # Check for number divisible by 2
    while number % 2 == 0:
        prime_factors.append(2)
        number //= 2

    # If number becomes 1 after division by 2
    if number == 1:
        return prime_factors

    #  we have checked for all the 2s now we will check for odd nums
    for i in range(3, int(number**0.5)+1, 2):
        while number % i == 0:
            prime_factors.append(i)
            number //= i

    # If N is still greater than 2, then N is prime
    if number > 2:
        prime_factors.append(number)

    return prime_factors

number_entered = input("Enter a number > 1 to get the prime factors: ")

number = (number_entered.isdigit()) and int(number_entered) or None


if number != None and number>1:
    print(get_prime_factors(number))
else:
    print(f"Invalid number {number_entered}. Please enter number > 1")