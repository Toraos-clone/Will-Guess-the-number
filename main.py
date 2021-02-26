#Now we're going to play another game, Guess the Number.

#The Python Program you create should start by generating a random number between 1 and 20.

#Then, the program should ask the user to guess the number. On each guess, it should tell you if the user's guess is "too low" or "too high". The game keeps repeating as the user enters the wrong guess.

#The game ends when the user enters the correct number, and it lets the user know so.

#Need to import random
import random
#need to set the random guess
secretNumber = random.randint(1, 21)
print(secretNumber)
#set the user guess to a default value that won't trigger the random guess and start a count of total guesses
userGuess = -1
count = 0
#start a while loop
while userGuess != secretNumber:

#ask for the user's guess
  userNumber = int(input("Enter a number between 1 and 20: "))


#compare the user's guess to the random
  if userNumber == secretNumber:
    count += 1

#if the user's guess is right, print end
    print(f"You guessed the secret number {secretNumber} in {count} guesses")
    break

# respond if the answer is too low and repeat
  elif userNumber < secretNumber:
    count += 1
    print("Your guess was too low")

#respond if the answer is too high and repeat
  else:
    count += 1
    print("You guessed too high")