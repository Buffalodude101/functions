# conversion calculator
# By: Hayden Hart

# user input regarding the length to convert
# get the unit from the user
# convert the length to the correct unit
# output the anwer to the user

user_len = float(input("Enter a length to convert "))
user_unit = input("What unit is your length? ")

# to convert inches to mm --> in X 25.4
# to convert mm to inches --> mm / 25.4

# user gives inches unit
convert_num = user_len * 25.4

print(user_unit)
print(convert_num)