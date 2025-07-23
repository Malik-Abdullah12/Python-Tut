#instructions given by video :
# You have to use a random choice function that we studied in tutorial #38, to select between, snake, water, and gun.
# You do not have to use a print statement in case of the above function.
# Then you have to give input from your side.
# After getting ten consecutive inputs, the computer will show the result based on each iteration.
# You have to use loops(while loop is preferred).
# Snake water gun
# Create a snake water gun game in Python! Search Snake water gun game in google if you need help on rules and how to play the game!

import random
rounds = 0 
computer_points = 0 
user_points = 0 

while True:
    while (rounds <= 10):
        p1 =  input("welcome to the game : snake water and gun, press \'s' for snake \n \'w' for water and \'g' for gun: \n")
        lst = ["snake", "water", "gun"]
        choice = random.choice(lst)
        if p1 == "s" and choice == "water":
            print("you won this round : snake drinks the water \n ")
            user_points += 1 
            rounds += 1 
        elif p1 == "s" and choice == "gun":
            print("you loose this round : gun shoots the snake its dead \n ")
            computer_points += 1 
            rounds += 1 
        elif p1 == "s" and choice == "snake":
            print("boths of our choices are same : its a draw \n ")
            rounds += 1 
        elif p1 == "w" and choice == "gun":
            print("you won this round : water swallows the gun \n ")
            user_points += 1 
            rounds += 1 
        elif p1 == "w" and choice == "water":
            print("boths of our choices are same : its a draw \n")
            rounds += 1 
        elif p1 == "w" and choice == "snake":
            print("you loose : snake drank all the water \n")
            computer_points += 1 
            rounds += 1 
        elif p1 == "g" and choice == "water":
            print("you loose : gun sink in the water \n ")
            computer_points += 1 
            rounds += 1 
        elif p1 == "g" and choice == "snake":
            print("you win this round  : gun shoots the snake its dead! \n ")
            user_points += 1 
            rounds += 1 
        elif p1 == "g" and choice == "gun":
            print("both of our choices were same its a draw \n ")
            rounds += 1 
        else :
            print("zida hooshiaari naa dikhaio jo poocha jarha sirf uska jawab do  \n")
        if rounds == 10:
            break
        else:
            continue


    print("computer has", computer_points, "points \n ")
    print("user has :", user_points, "points \n ")

    if computer_points> user_points:
        print("you lost the game computer won \n ")
    elif computer_points < user_points:
        print("you won the game computer lost the game \n ")
    else:
        print("its a draw")

    p2 = input("press (y) to continue and (e) for exit ")
    if p2 == "y":
        # Continue with your desired action here
        print("Continuing...")
    elif p2 == "e":
        # Exit the loop when 'e' is entered
        print("Exiting...")
        break
    else:
        p2 = input("press (y) to continue and (e) for exit ")
        if p2 == "y":
        # Continue with your desired action here
            print("Continuing...")
        elif p2 == "e":
        # Exit the loop when 'e' is entered
            print("Exiting...")
        break
      # Ignore any other input and ask for input again


        








    
    




