secret_fruit = "banana"
guess = ""
guess_count = 0
guess_limit = 4 
while guess != secret_fruit and guess_count < guess_limit:
    guess = input("Guess the fruit: ")
    guess_count += 1

if guess == secret_fruit:
    print("Congratulations! You guessed the fruit.")
else:
    print("Sorry, you ran out of guesses.")