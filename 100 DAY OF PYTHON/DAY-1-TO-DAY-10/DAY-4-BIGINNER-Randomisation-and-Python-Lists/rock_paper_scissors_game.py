import random
import my_module

user_choose = int(input("Choose 0 for rock, 1 for paper and 2 for scissors:\n"))

computer_choice = random.randint(0, 2)
# print(random_rock_paper_scissors)

if user_choose == 0:
    print(my_module.rock_arts)
elif user_choose == 1:
    print(my_module.paper_arts)
elif user_choose == 2:
    print(my_module.scissors_arts)
else:
    print("Incorrect hand, you lose.")

if computer_choice == 0:
    print("""
    Computer choose:
          """)
    print(my_module.rock_arts)
elif computer_choice == 1:
    print("""
       Computer choose:
             """)
    print(my_module.paper_arts)
elif computer_choice == 2:
    print("""
       Computer choose:
             """)
    print(my_module.scissors_arts)

if user_choose == computer_choice:
    print("Tie")
elif user_choose == 0 and computer_choice == 2:
    print("You win!")
elif user_choose == 2 and computer_choice == 1:
    print("You win!")
elif user_choose == 1 and computer_choice == 0:
    print("You win!")
else:
    print("You lose!")
