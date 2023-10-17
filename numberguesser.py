import random
print()
print()
#Display of game title.
print("GUESS THE NUMBER:")
print("------------------")
#Display of welcome message/directions.
print("Directions:")
print("* Player enters the upper bounds of the range starting from 1.")
print("* Try to guess the number between this range.")
print("* You get ten tries.")
print()

#Core of the game.
while True:
	high_num = int(input(f"\nEnter higher range: "))
	random_num = random.randint(1,high_num)
	attempts = 0

	print(f"\nI'm thinking of a number from 1 to", high_num,".....\n")

	while attempts < 10 or guess == random_num:
		#Feedback after every round. 
		guess = int(input("Your guess: "))
		attempts = attempts + 1 
		if guess < 1 or guess > high_num:
			print("Invalid input. Please enter a number to try again.")
		elif guess < random_num:
			print("Too low. Try again.")
		elif guess > random_num:
			print("Too high. Try again.")
		else:
			if attempts == 1:
				print(f"You guessed it in {attempts} try!")
			else:
				print(f"You guessed it in {attempts} tries!")
			break
			#If guess is correct, break the loop.
		    
		if attempts >= 10:
			print("Too many tries. You lost.")

	again = input(f"\nWould you like to play again? (y/n): ")
	if again.lower() != "y":
		print(f"\nBye!\n")
		break
		#If player does not want to play again, break the loop and end the game/program. 
