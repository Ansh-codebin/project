import random


user_input= input("enter a choise:rock,paper,scissors")
possible_action=["rock" , "paper" , "scissors"]
computer_action = random.choice(possible_action)

print(computer_action)



if user_input==computer_action:
    print("tie")

elif user_input=="rock"and computer_action=="scissors":
    print("victory")

elif user_input=="paper"and computer_action=="rock":
    print("victory")


elif user_input=="scissors"and computer_action=="paper":
    print("victory")

else:
    print("lose")   