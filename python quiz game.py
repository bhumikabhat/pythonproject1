# python quiz game

questions =("What is the capital of India?: ",
            "Which planet is known as the Red Planet?: ",
            "Which is the largest mammal in the world?: ",
            "How many continents are there in the world?: ",
            "Who wrote Romeo and Juliet?: ")

options =(("A. Mumbai", "B. Delhi", "C. Nagpur", "D. Kolkata"),
          ("A. Jupiter", "B. Mercury", "C. Mars", "D. Earth"),
          ("A. Blue Whale", "B. Elephant", "C. Lion", "D. Dolphin"),
          ("A. 8", "B. 10", "C. 7", "D. 6"),
          ("A. Charles Dickens", "B. Stephen king", "C. J.K Rowling", "D. William Shakespeare"))

answers = ("B", "C", "A", "C", "D")
guesses =[]
score = 0
question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
         score += 1
         print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("----------------------------")
print("           RESULTS          ")
print("----------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/ len(questions) * 100)
print(f"Your score is: {score}%")