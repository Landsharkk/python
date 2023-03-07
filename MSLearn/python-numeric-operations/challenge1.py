ftemp = input('What is the temperature in fahrenheit? ')

if ftemp.isnumeric() == False:
    print('Value entered is not a number.')
    exit()


ctemp = ((int(ftemp) - 32) * 5/9)

print('Temperature in celsius is ' + str(ctemp))