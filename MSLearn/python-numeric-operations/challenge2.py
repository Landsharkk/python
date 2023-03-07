print('Simple Calculator!\n ')
first_number = input('First Number: ') 
second_number = input('Second Number: ')
#could have casted first_number and second_number as int directly after taking them as input # to avoid casting int() in the if loop.
calc_type = input('Operation (+, -, *, /, %, **): ')

if first_number.isnumeric() == False or second_number.isnumeric() == False:
    print('Value entered was not a number.')
    exit()

if calc_type != '+' or '-' or '*' or '/' or '%' or '**':
    print('Operation not recognized.')

if calc_type == '+':
    result = int(first_number) + int(second_number)
elif calc_type == '-':
    result = int(first_number) - int(second_number)
elif calc_type == '*':
    result = int(first_number) * int(second_number)
elif calc_type == '/':
    result = int(first_number) / int(second_number)
elif calc_type == '%':
    result = int(first_number) % int(second_number)
elif calc_type == '**':
    result = int(first_number) ** int(second_number)
#could have ended with else: print('command not recognized') to avoid having to validate calc_type before the if loop

print('Product of ' + str(first_number) + ' ' + str(calc_type) + ' ' + str(second_number) + ' equals: ' + str(result))



"""
Output Example:
Simple calculator!
First numer? 4
Operation? *
Second number? 5
Product of 4 * 5 equals 20
"""
