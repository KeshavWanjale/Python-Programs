'''
Write a program WindChill.java that takes two double command-line arguments t
and v and prints the wind chill. Use Math.pow(a, b) to compute ab. Given the
temperature t (in Fahrenheit) and the wind speed v (in miles per hour), the
National Weather Service defines the effective temperature (the wind chill) to be:
wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 
             0.4275 * temperature * (wind_speed ** 0.16)
Note: the formula is not valid if t is larger than 50 in absolute value or if v is larger
than 120 or less than 3 (you may assume that the values you get are in that range).
'''
month_entered = input("Enter the month number (1 to 12): ")

month = month_entered.isdigit() and int(month_entered) or None
    

if month != None and month in [11,12,1,2]:
    temprature_entered = input("Enter the temperature between -50 and 50 °F: ")
    wind_speed_entered = input("Enter the wind speed between 3 and 120 mph: ")

    temperature = temprature_entered.isdigit() and int(temprature_entered) or None
    wind_speed = wind_speed_entered.isdigit() and int(wind_speed_entered) or None

    if temperature == None:
        print(f"Invalid input {temprature_entered}. Enter Valid Temperature")
    elif wind_speed == None:
        print(f"Invalid input {wind_speed_entered}. Enter Valid Wind speed")
    elif abs(temperature) > 50 or wind_speed < 3 or wind_speed >120  :
        print(f"Invalid input. Temperature {temperature} must be between -50 and 50 °F",
                f", and wind speed {wind_speed} between 3 and 120 mph")
    else:
        wind_chill = (35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) +
                        0.4275 * temperature * (wind_speed ** 0.16))
        print(f"Wind Chill: {wind_chill:.02f} °F for Month {month} with "
            f"temperature {temperature} and wind speed {wind_speed}")

else:
    print(f"Wind chill computation is not applicable for month {month_entered}t.")