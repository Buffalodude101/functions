# conversion calculator
# By: Hayden Hart

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the anwer to the user

while True:
    while True:
        user_len = (input("Enter a whole number to convert "))
        if user_len.isdigit():
            user_len = float(user_len)
            break
        else:
            print("Please try agian")
        
        
       



    user_unit = input("What unit is your length? ")

    # to convert inches to mm --> in X 25.4
    # to convert mm to inches --> mm / 25.4

    # user gives inches unit

    if user_unit == 'in':
        convert_num = user_len * 25.4
        convert_unit = 'mm'
        break
    elif user_unit == 'mm':
        convert_num = user_len / 25.4
        convert_unit = 'in'
        break
    else:
        print("Invalid unit")


print(f"{convert_num:.2f}{convert_unit}")