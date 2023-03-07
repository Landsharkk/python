first_value = ' FIRST challenge     '
second_value = '- second challenge -'
third_value = 'tH IR D-C HALLE NGE'

fourth_value = 'fourth'
fifth_value = 'fifth'
sixth_value = 'sixth'

# First challenge

first_value = first_value.lstrip()
first_value = first_value.title()
first_value = f'{first_value:^30}'


# Second Challenge
second_value = second_value.replace('-', '')
second_value = second_value.lstrip()
second_value = second_value.capitalize()

# Third Challenge
third_value = third_value.replace(' ','')
third_value = third_value.replace('-',' ')
third_value = third_value.lower()
third_value = third_value.capitalize()
third_value = f'{third_value:>30}'


print(first_value)
print(second_value)
print(third_value)

# Fourth Challenge - use only the print() function (no f-strings)
print(fourth_value + "#" + fifth_value + "#" + sixth_value + "!")

# Fifth Challenge - use only a single print() function.  Create tabs and new lines using f-strings.
print(f'{fourth_value:^30}\n', f'{fifth_value:^30}\n',f'{fifth_value:^30}\n')

print(f'\n\t{fourth_value}\n\t{fifth_value}\n\t{sixth_value}')

