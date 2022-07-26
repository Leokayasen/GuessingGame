import random
# ∆ Imports a randomiser
randNum = random.randint(1,100)
# ∆ Generates a random number between 1 and 100
guessInput = False
for go in range(10):
	guessInput = int(input("I think of a number, between 1 and 100. Guess the number: "))
  # ∆ User must enter a number to guess what the generator made
	if guessInput == randNum:
		guessInput = True
		break
	elif guessInput > randNum:
		print("Too High")
    # ∆ When user input for guess is higher than randNum, say the above
	else:
		print("Too Low")
    # ∆ When user input for guess is lower than randNum, say the above
if randNum:
	print("Correct")
else:
	print("Number was ", randNum)
  # ∆ When the game ends, it will output randNum, as long as user does not make a correct guess
