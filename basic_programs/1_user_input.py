'''
1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
    a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
    b. Logic -> Replace <<UserName>> with the proper name
    c. O/P -> Print the String with User Name

'''
# Taking user name input
user_name_input = input("Enter User Name: ")

# check if char is >= 3
# Short circuit if
user_name = len(user_name_input)>=3 and user_name_input or None

if user_name != None:
    print(f"Hello {user_name}, How are you?")
else:
    print(f"Invalid input User Name:{user_name_input}. Must have atleast 3 characters.")