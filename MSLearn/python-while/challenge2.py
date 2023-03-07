import random

roll = 0
count = 0
winningnumber = random.randint(1, 10)
print(f'PC chose number {winningnumber}')
print('Guess a numbet between 1 and 10')
while roll != winningnumber:
    count += 1
    roll = input(f'Enter guess #{count}: ')
    if roll.isnumeric():
        roll = int(roll)
        if roll < winningnumber:
            print('Your guess is too low, try again!')
        elif roll > winningnumber:
            print('Your guess is too high, try again!')
    else:
        print('Numbers only, please!')
        continue

print(f'You guess it in {count} tries! The number was {winningnumber}.')