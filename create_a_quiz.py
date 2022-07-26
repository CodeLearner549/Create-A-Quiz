# Create-A-Quiz

print("WELCOME TO THE RANDOM QUIZ")

score = 0

answer1 = input("What is 1 + 1? ")
if answer1.lower() == "two" or answer1 == "2":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer2 = input("What is the capital of Canada? ")
if answer2.lower() == "ottowa":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer3 = input("What is 2 + 2? ")
if answer3.lower() == "four" or answer3 == "4":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer4 = input("What is the Capital of Japan? ")
if answer4.lower() == "tokyo":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

answer5 = input("Who is the best computer science teacher? ")
if answer5.lower() == "mr. v" or answer5.lower() == "mr. velkamp" or answer5.lower() == "mr.v" or answer5.lower() == "mr.veldkamp":
    print("Correct")
    score = score + 1
else:
    print("Incorrect")

percentage = score / 5 * 100

print("Your score is " + str(score) + "/5" +
      " (" + str(percentage) + "%" + ").")

if percentage == 100:
    print("Nice.")
elif percentage > 50 and percentage < 100:
    print("Needs Work.")
else:
    print("Ridiculous.")
