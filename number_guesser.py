import random

top_of_range = input("Type a number: ")

number_of_guesses=0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number =random.randint(0,top_of_range)

while True:
    number_of_guesses+=1
    user_guess=input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue
    if user_guess == random_number:
        print("your guess is right!!")
        print(f"you got it in {number_of_guesses} guesses")
        break
    elif user_guess >random_number:
        print("you got it above the number!")
    else:
        print("you got it below the number!")   



