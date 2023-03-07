print("Today's date?")
date = input()
print (date)

print("Breakfast calories?")
b_calories = int(input())
print (b_calories)

print("Lunch calories?")
l_calories = int(input())
print (l_calories)

print ("Dinner calories?")
d_calories = int(input())
print (d_calories)

print ("Snack calories?")
s_calories = int(input())
print (s_calories)

sum = b_calories + l_calories + d_calories + s_calories
print ("Calorie count for " + str(date) + " :" + str(sum))
