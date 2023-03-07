"""
numeric_value = '7'
print(numeric_value.isnumeric())

string_value = 'Bob'
print(string_value.isnumeric())
"""

first_value = input('First Number: ')
second_value = input('Second Number: ')

#format the input to remove spaces before and after the input from user
first_value = first_value.replace(' ', '')
second_value = second_value.replace(' ', '')

if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print('Value is not a number.')
    exit()

first_value = int(first_value)
second_value = int(second_value)

sum = first_value + second_value
print('Sum: ' + str(sum))


