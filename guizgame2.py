print("Welcome to the Quiz Game")

playing = input("Do you want to play? ")
if playing != "yes":
    quit()

print("Okay! Let's Play")
score=0

answer = input("What is the Captial of India? ")
if answer == "Delhi" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does CPU stands for? ")
if answer.lower() == "Central Processing Unit" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Which is the World's Oldest Language in the World? ")
if answer.lower() == "Tamil" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("Where does the Gate Way of India Located? ")
if answer.lower() == "Mumbai" :
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct")
print("You got " + str(score/4 * 100) + " questions correct")
