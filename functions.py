# conversion calculator
# By: Hayden Hart

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the anwer to the user

def user_parser(user_input):
    values = user_input.rsplit(" ")
    number = values[0]
    if number.isdigit():
        number = float(number)
    else:
        print("That is not a valid number ")
    unit = values[1]
    if unit != "IN":
        print("That is not a valid unit")
    return number, unit
    

    
    #print(f"{values[0]} {values[1]}")



while True:
    user_len = input("number and unit to convert ").upper()
    user_number, user_unit = user_parser(user_len)
    print("User number", user_number)
    print("User unit", user_unit)

#     while ValueError:
#         try:
#              user_len = float(input("Enter a whole number to convert "))
#              if user_len != ValueError:
#                 break
#         #if user_len.isdigit():
#             #user_len = float(user_len)
#             #break
#         #else:
#            # print("Please try agian")
#         except ValueError as err:
#             print(err)
        
        
       



#     user_unit = input("What unit is your length? ")

#     # to convert inches to mm --> in X 25.4
#     # to convert mm to inches --> mm / 25.4

#     # user gives inches unit

#     if user_unit == 'in':
#         convert_num = user_len * 25.4
#         convert_unit = 'mm'
#         break
#     elif user_unit == 'mm':
#         convert_num = user_len / 25.4
#         convert_unit = 'in'
#         break
#     else:
#         print("Invalid unit")


print(f"{convert_num:.2f}{convert_unit}")