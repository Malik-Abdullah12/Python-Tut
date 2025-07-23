# excersize 2: faulty calculator!
# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
print("welcome to the best calculator for math test ")
print("what two numbers u like to operate on")
n1 = int(input())
n2 = int(input())
print("what operator do u like to use(+,-,*,/)")
op = input()

if (n1,n2)==(45,3) and op=="*":
    print("555")
elif (n1,n2)==(56,9) and op=="+":
    print("77")
elif (n1,n2)==(56,6) and op=="/":
    print("4")
else:
    if op=="+":
        print(n1 + n2)
    elif op=="-":
        print(n1 - n2)
    elif op=="*":
        print(n1 * n2)
    elif op=="/":
        print(n1 / n2)
    else:
        print("enter a valid function to operate")
