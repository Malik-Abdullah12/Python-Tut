
# exercize 3 : guess the numbers:
# no of guesses 9 
# print number of guesses left 
# no of guesses he took to finish
# game over
# n = 10
# print("lets play a game of guessing numbers ")
# print("no of guesses are 9")
# while (True):
#     p1 = int(input("guess the number ? \n "))
#     if p1==n:
#         print("u have guessed the number")
#         break
#     elif p1>n:
#         print("no its lower")
#         if p1<n:
#             print("no its higher")
#             if p1==(7   or   12):
#                 print("you are so close ")
#             else:
#                 continue

# n = 20 
# g = 1
# print("lets a play a game of guessing the number ","there are 9 attempts ")
# while (g<=9):
#     p1 = int(input("guess the number: \n"))
#     if p1<n:
#         print("no its a greater  number try again: \n ")
#     elif p1>n:
#         print("no its a lesser number try again ")
#     elif p1==n:
#         print("congrats u have guessed the number ")
#         print(g,"no of guesses u took to complete ")
#         break
#     else:
#         print("invalid")
#     print(9-g,"number of guesses left \n")
#     g = g + 1

# if (g>9):
#     print("game_over")

        
# i = 0
# while(i<100):
#     i = i + 1
#     if (i>98):
#         break
#     print(i)

# n = 18 
# g = 1
# print("lets play a game of guessing number ")
# print("warning u will only have 9 attmepts you will judged by that ")
# while (g<=9):
#     p2 = int(input("ok now guess the number its in between 1 to 100 \n"))
#     if (p2>n):
#         print("its an higher number that u picked!\n sorry plz try again ")
#     elif (p2<n):
#         print("u have entered a lesser number\n plz try again\n ")
#     else:
#         print("congrats u finally have won the game wohooooooo\n ")
#         print(g," number of guesses u took to complete the game\n")
#         break
#     print(9-g, "number of guesses left ")
#     g = g + 1 
# if (g>9):
#     print("game over you lost ")


n = 18

turn = 1

print("lets a play game of guessing number  : \n")
print("u will have 9 attempts")
print(" game of guessing number  : \n")
print("u will have 9 attempts")

while(turn<=9):

    p1 = int(input("now guess the number its in between 1 to 50"))
    if p1>n:
        print("wrong answer : u picked a higher number try again ")
    elif p1<n:
        print("wrong answer : u picked a lower number try again ")
    else:
        print("congrats u won the gqame ")
        print(turn,"number of guesses u took to win ")
        break

    print(9-turn, "numbers of guesses left ; ")
    turn = turn + 1

if (turn>9):
    print("game over : ")



# def calculator():
#     print("welcome  to the calculator ")
    
#     a= int(input("enter first number "))

#     b= int(input("enter ur second number "))
#     c = input("what operator do u like to choose : ")

#     if c == "+":
#         print("the answer of your sum is  :", a + b )
    
#     elif c == "-":
#         print("the answer of your sum is  :", a - b )
    
#     elif c == "*":
#         print("the answer of your sum is  :", a * b )

#     elif c == "/":
#         print("the answer of your sum is  :", a / b )

#     else:
#         print("wrong input command  :")
#         print("exiting : ")

# calculator()
    

















