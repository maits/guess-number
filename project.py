import random, sys

name = raw_input("Hello! What's your name?: ")
can = raw_input("Hello {0}, I'm thinking about a number from 1 to 100. Can you guess it? [Y|N]:".format(name))

if can != "Y" and can != "y" :
	print "OK! Good bye ..."
	sys.exit(1)

variable = random.randint(0, 10)
guesses = 0

while True :
	
	x = input('Guess a number: ')
	guesses += 1
	print "You chose", x
	
	if variable > x:
		print("Your number is too low.")

	if variable < x:
		print("Your number is too high.")

	if variable == x:
		print("You got it right!")
		break

print "You guessed {0} times! Good work!".format(guesses)
