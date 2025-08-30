import random
while True:
    user_imp = input("Roll the dice(yes/no)?: ").lower()
    if user_imp == "yes":
        print(f"The number you've rolled is,{random.randint(1,7)}")
    elif user_imp == "no":
        print("Thanks for playing!")
        break
    else:
        print('please enter a valid command')

