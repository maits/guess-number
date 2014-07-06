import random

variable = random.randint(0, 10) 
x = input('Guess a number from 1 to 10: ')
print "You chose", x

if variable > x:
	print("Your number is too low.")

if variable < x:
	print("Your number is too high.")

if variable == x:
	print("You got it right!")

print "The correct number is..."
print "*drumroll*"
print variable

