# Health Management System
# 3 clients - Harry, Rohan and Hammad

# def getdate():
#     import datetime
#     return datetime.datetime.now()
# print(getdate())


# def function1():
#     p1 = input("enter client name: \n ")
#     p2 = int(input("what would u like to lock 'diet' or 'exercize' \n for diet press 1 and exercize press 2 " ))
#     if (p1,p2)==("hammad",1):
#         p3 = input("input data ")
#         f = open("hammad_food.py", "a")
#         p3 = f 
#         print(f)
#         import datetime
#     return datetime.datetime.now()
        
# print(function1())


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client

import datetime
def gettime():
    return datetime.datetime.now()
def take(d):
    if d==1:
        f = int(input("press 1 for food 2 for exercize"))
        if f == 1:
            value = input("type here ")
            with open("harry_food.py", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + '\n')
                print('successfully written')
        elif f==2:
            value = input("type here ")
            with open("harry_ex.py", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + '\n')
                print('successfully written')
    elif d==2:
         f = int(input("press 1 for food 2 for exercize"))
         if f == 1:
            value = input("type here ")
            with open("rohan_food.py", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + '\n')
                print('successfully written')
         if f== 2:
             value = input("type here ")
             with open("rohan_ex.py", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + '\n')
                print('successfully written')
    elif d == 3:
         f = int(input("press 1 for food 2 for exercize"))
         if f == 1:
            value = input("type here ")
            with open("hammad_food.py", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + '\n')
                print('successfully written')
         if f== 2:
             value = input("type here ")
             with open("hammad_ex.py", "a") as op:
                op.write(str([str(gettime())]) + ":" + value + '\n')
                print('successfully written')
    else:
        print('enter a valid input command [1:harry], [2:rohan] , [3:hammad]')

def retrieve(d):
    if d==1:
        f=int(input("enter 1 for food 2 for exercize"))
        if(f==1):
            with open("harry_food.py") as op:
                for i in op:
                    print(i, end="")
        elif(f==2):
            with open("harry_ex.py") as op:
                for i in op:
                    print(i,end="")
    elif(d==2):
        f = int(input("enter 1 for food and 2 for exercize "))
        if (f == 1):
            with open("rohan_food.py") as op:
                for i in op:
                    print(i, end="")
        elif (f == 2):
            with open("rohan_ex.py") as op:
                for i in op:
                    print(i, end="")
    elif(d==3):
        f = int(input("enter 1 for food and 2 for exercize"))
        if (f == 1):
            with open("hammad_food.py") as op:
                for i in op:
                    print(i, end="")
        elif (f == 2):
             with open("hammad_ex.py") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")

print("welcome to health management system \n follow the instructions given below \n enter your data or retrieve it")
 
a  = int(input("press 1 for log or 2 for retrieve the value "))

if a == 1 :
    d = int(input("press 1 for harry 2 for rohan and 3 for hammad "))
    take(d)

if a == 2 :
     d = int(input("press 1 for harry 2 for rohan and 3 for hammad "))
     retrieve(d)
    

             
         
        



  
