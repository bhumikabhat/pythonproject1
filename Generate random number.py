import random

#number = random.randint(1, 6)

#print(number)

#ow = 1
#high = 100  
#options = ("rock", "paper", "scissors")
#cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

#number = random.randint(low, high)
#number = random.random()

#print(number)

#option = random.choice(options)

#print(option)

#random.shuffle(cards)
#print(cards)

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f"Enter a number between ({low} - {high}): "))
    guesses += 1

    if guess < number:
        print(f"{guess} is too low")
    elif guess > number:
        print(f"{guess} is too high")
    else:
        print(f"{guess} is correct")
        break

print(f"This round took you {guesses} guesses")