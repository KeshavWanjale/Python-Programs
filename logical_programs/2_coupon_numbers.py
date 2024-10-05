'''
2. Coupon Numbers
    a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
    need to generate distinct coupon number? This program simulates this random
    process.
    b. I/P -> N Distinct Coupon Number
    c. Logic -> repeatedly choose a random number and check whether it's a new one.
    d. O/P -> total random number needed to have all distinct numbers.
    e. Functions => Write Class Static Functions to generate random number and to
    process distinct coupons
'''
import random
def get_distinct_coupons(number):
    distinct_coupons = set()
    total_random_numbers = 0
    
    # Keep generating random numbers until we collect all N distinct coupons
    while len(distinct_coupons) < number:
        coupon = random.randint(0,number)
        total_random_numbers += 1
        
        distinct_coupons.add(coupon)
    
    print(f"Total random number needed: {total_random_numbers}")

get_distinct_coupons(10)