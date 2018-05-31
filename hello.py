#!/usr/bin/env python3
mood = input("How the hell are ya?: ")
if mood == ('good'):
    print("That's great!")
elif mood == ('bad'):
    print("That's no good!")
else:
    print("I don't know what to say!")
age = input("How old are you?")
age2 = int(age) + 1
print("So that means that in one year you'll be " + str(age2) + ", right?")
print(mood)

