print("Welcome to the Quiz Game!")
playing= input("Do you want to play? (type 'yes' to continue): ")

if playing!= "yes":
    quit()
else:
    print("Okay, let's start!")
    print("Note: Please answer the following questions in all lower case.")
score=0

ans1= input("What is the full form of CPU?: ")
if ans1=="central processing unit":
    print("Correct!")
    score +=10
else:
    print("Wrong:(")
print(score)

ans2= input("What does RAM stand for?: ")
if ans2=="random access memory":
    print("Correct!")
else:
    print("Wrong:(")

ans3= input("What is the full form of GPU?: ")
if ans3=="graphics processing unit":
    print("Correct!")
else:
    print("Wrong:(")

ans4= input("What does PSU stand for?: ")
if ans4=="power supply unit":
    print("Correct!")
else:
    print("Wrong:(")