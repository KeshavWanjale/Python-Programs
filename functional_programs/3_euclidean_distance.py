'''
Write a program Distance.java that takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
'''
def get_euclidean_distance(x,y):
    # returns Euclidean distance from the point (x, y) to the origin (0, 0)
    return float(((x**2)+(y**2))**0.5)

number_entered_x = input("Enter a number > 0 to Euclidean distance: ")
number_entered_y = input("Enter a number > 0 to Euclidean distance: ")

number_x = (number_entered_x.isdigit()) and int(number_entered_x) or None
number_y = (number_entered_y.isdigit()) and int(number_entered_y) or None

if (number_x != None and number_y != None) and (number_x>0 and number_y>0):
    print(f"Euclidean distance from point ({number_x},{number_y}) to its origin (0,0) is",
           f"{get_euclidean_distance(number_x,number_y):.2f}")
else:
    print(f"Invalid number {number_entered_x}, {number_entered_y}. Please enter number > 0")