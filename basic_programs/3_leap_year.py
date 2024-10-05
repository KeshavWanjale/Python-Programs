'''
3. Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not.
'''
def is_leap_year(year : int) :
  if year < 1582 :
    return f"Invalid Year {year} entered. Must be 1582 or Later"
  if(year % 100 == 0) and (year % 400 == 0) :
    return f"The Year {year} is a Leap Year"
  if (year % 4 == 0) and (year % 100 != 0) :
    return f"The Year {year} is a Leap Year"
  return f"The Year {year} is not a Leap Year"

year_entered = input(f"Enter a year: ")

year = (year_entered.isdigit() and len(year_entered)>= 4) and int(year_entered) or None
if year != None:
  print(is_leap_year(year))
else:
  print("Invalid input year must be number having four digits.")