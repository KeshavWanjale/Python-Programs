'''
Write a program Quadratic.java to find the roots of the equation a*x*x + b*x + c.
Since the equation is x*x, hence there are 2 roots. The 2 roots of the equation
can be found using a formula (Note: Take a, b and c as input values)
delta = b*b - 4*a*c
Root 1 of x = (-b + sqrt(delta))/(2*a)
Root 2 of x = (-b - sqrt(delta))/(2*a)
'''

def get_roots(a,b,c):
    delta = b*b - 4*a*b
    root1 = (-b + (delta ** 0.5))/(2*a)
    root2 = (-b - (delta ** 0.5))/(2*a)
    return root1,root2

print(f"{get_roots(1,5,6)}")