import random

count = 0
roll = 0
winningnumber = random.randint(1,5)
print('the computer chose ' + str(winningnumber))
while roll != winningnumber:
    count += 1
    roll = input('Guess a number between 1 and 5: ')
    if roll.isnumeric() and int(roll) == winningnumber:
        print(f'You guess the correct number, it was {winningnumber}!')
        break
    else:
        continue

print(f'You guess it in {count} tries!')







"""
Guess a number between 1 and 5: 3
Guess a number between 1 and 5: 4
You guessed it in 2 tries!
"""