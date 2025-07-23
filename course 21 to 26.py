# # tut 21 operators in python:
# #arithmetic operators:
# print("arithmetic operators: ")
# print("5 + 6 is ", 5+6)
# print("5 - 6 is ", 5-6)
# print("5 * 6 is ", 5*6)
# print("5 / 6 is ", 5/6)
# print("5 // 6 is ", 5//6)#gives the result in round figure of integers
# print("5 ** 3 is ", 5**3)#its use for power of a number
# print("5 % 6 is ", 5%6)#modulus tells us the remainder of the result

# #assignment operators :
# print("assignment operators: ")
# x = 5 #assignment operators are used to assign value to objects 
# print(x)
# x = x + 7
# print(x)
# x += 10
# print(x)
# x += 9
# print(x)
# x -= 9
# print(x)
# x /= 9
# print(x)
# x *= 9
# print(x)

# #comparison operators:
# print("comparison operators ")
# #it tells the value is wether true statement or not it compares the value to each other.
# i = 5 
# print(i<=5)#it tells the condition wether its true or not 
# print(i>5)


# logical operators :
# logical operators are "and" and "or" function to give the statement true or false 
# a = True
# b = False
# print(a)
# print(a and b )#and function checks both the value if one is false it will be false 
# print(a or b )# in or if one is true it will be true 
# identity operators:
# these operators are "is " and "not".


# a=5
# b=5

# print(a is not b)
    # print('yes')
# else:
    # print('no')

# print(5 != 5)#if the value is not equal to equal it will print false
# print(5 is not 5 )#if it is then it will be true 

#membership operators:
# these are use to tell u that in a data the member u are looking for is there or not.

# list1 = [23,3434,545,64,23,43,65]
# print(87  not in list1)#hence the value is not there but the command is not so it will be true
# print(545   in list1)#there 545 is the member of the list so it will print true to the statement 

# Bitwise Operators
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

# print(0 & 2)
# print(0 | 3)


# #tut 22 python: short hand if else notation:
# a = int(input("enter a \n"))
# b = int(input("enter b \n"))
# # if a<b: print("a is lesser than b ")#this is called short hand notation
# # else: print("b is lesser than a ")#u can also use short hand notation for your readability
# print("a is lesser than b ") if a<b else print("b is lesser bhaii hoosh mi ho  ")
# # u can also use like this to your coding hence its better to avoid it to your prespective 
# #normal code is mcuh prefeable or u can also use this for shorter program or to your udnerstanding 

# tut: 23 : functions and docstrings 
# a = 5 
# b = 61
# c = sum((a,b))#sum function should be iterable means u can use list or tuppel to run it 
# print(c)#sum is a built in function


#function test 
# def function1():
#     print("this is a user define function")
# function1()


#function for displaying your name.
# def ab(name):   
#     print(input('My name is',name))

# ab(23)


# function for  asking your name from user (input use)
# def function2():
#     p1 = input("whats your name\n ")
#     print("your name is ", p1)
# function2()


# function for sum of a,b
# def function3(a,b):
#     print("the answer of a and b sum is ", a + b)
# function3(56,34)


# simple calculator from function:
# print("welcome to simple calculator")
# def function4():
#     p2= int(input("enter your first number\n"))
#     p3= int(input("enter your second number\n"))
#     p4= input("enter the operator u like to choose \n")
#     if p4=="+":
#         print("your answer is ",p2 + p3)
#     elif p4=="-":
#         print("your answer is ", p2 - p3)
#     elif p4=="*":
#         print("your answer is ", p2 * p3)
#     elif p4=="/":
#         print("your answer is ", p2 / p3)
#     else:
#         print("not valid command")
# function4()

#function for average of two numbers:
# def function5(a,b):
#     average = a+b/2
#     # print(average)
#     # print("print ")
#     return average   #A return is a value that a function returns to the calling script or function when it completes its task. 
# s= function5(6767,908776)
# print(s)

# def function4(c,d):
#     multiply = c*d
#     return multiply
# q = function4(3,4)
# print(q)

# def function6():
#     """this is a function that takes input of two numbers and give average 
#     $note:its for only two numbers it will not work on three numbers"""#a docstring is a string literal specified in source code that is used, like a comment, to document a specific segment of code
#     s1 = int(input("enter your first number\n "))
#     s2 = int(input("enter your second number\n "))
#     print("the average of these numbers is", s1+s2/2)

# print(function6.__doc__)#its the syntax thats how u call a docstring from a def function
# function6()

#tut24:try except exception handling in python:

# """The try block lets you test a block of code for errors.
#  The except block lets you handle the error. The else block
#    lets you execute code when there is no error. The finally block lets
#      you execute code, regardless of the result of the try- and except blocks."""
# while True:
#     print("Enter num 1")
#     num1 = input()
#     print("Enter num 2")
#     num2 = input()
#     try:
#         print("The sum of these two numbers is",
#             int(num1)/int(num2))
#     except Exception as s:
#          print(s)
#     print("This line is very important")
#     break
 

# list2 = []
# while(True):
#     list1 = []
#     p1 = input('enter your ID press 00 for exit:')
#     if p1=="00":
#         break
#     p2 = input('enter your name')
#     list1.append(p1)
#     list1.append(p2)
#     print(list1)
#     list2.append(list1)
    # print(list2)
   

# addd function
# def function7(list2):
#     list1 = []
    
#     p1 = input('enter your ID:')
#     p2 = input('enter your NAME:')
#     list1.append(p1)
#     list1.append(p2)
#     # print(list1)
#     list2.append(list1)
#     # print(list2)
#     return list1, list2

# def delete(x,y):
#     print(x,y)
#     # Search by id
#     # if id matches remove that list from the list of list


# # delete fucntion

# list1 = []
# list2 = []
# p1 = input('enter your ID:')
# p2 = input('enter your NAME:')
# list1.pop(0)
# list1.pop(1)
# print(list1)
# list2.append(list1)
# print(list2)

# while True:
#     list2 = []
    
#     while True:
#         x, y = function7(list2)
#         delete(x,y)

#tut 25 file IO basics :

"""
r : r mode opens a file for read-only. We do not have permission to update or change any data in this mode.
w : w mode does not concern itself with what is present in the file. It just opens a file for writing and if there is
 already some data present in the file, it overwrites it.
x : x is used to create a new file. It does not work for an already existing file, as in such
 cases the operation fails.
a : a stands for append, which means to add something to the end of the file. It does exactly the same. It just adds 
the data we like in write(w) mode but instead of overwriting it just adds it to the end of the file. It also does not
 have the permission of reading the file.
t : t mode is used to open our file in text mode and only proper text files can be opened by it. It deals
 with the file data as a string.
b : b stands for binary and this mode can only open the binary files, that are read in bytes.
 The binary files include images, documents, or all other files that require specific software to be read.
+ : In plus mode, we can read and write a file simultaneously. The mode is mostly used 
in cases where we want to update our file."""

# tut:26 Open(), Read() & Readline() For Reading File ::

# f = open('tes.py','rt')
# print(f.readline())
# print(f.readline())#this can also use to print the file in readline.
# print(f.readline())#///////////////////////////////////////////////
# print(f.readlines())#to read the data in list form 

# content = f.read()#code to print the content 
# content = f.readline()#its used to read a line of a file command

# print(content)#code to print the content
# for line in f:
    # print(line, end="")#this is how u can read all the data in lines command:
# f.close()#we should close the command or u can say file at the end




 





l1 = [10,50,54,30,998898,23,5,100,9]
l2 = []


max=l1[0]
s_max= 0


for i in l1:

    if i > max:
        
        max = i 
        # value_remove = max
        # l1.remove(max)




# for num in l1 :
#     if num != max:
#         l2.append(num)

# for num in l2 :
#     if num > s_max:
#         s_max = num

# print("second high: ",s_max)
# print("max value : ",max)
# print(l2)    /

# print(s1)
# print(max)
# print(sec_h)
# print(l1)

    # if l1 > i:
    #     sec_h = i 
        # value_remove = max
        # l1.remove(max)

    # else:
    #     max1 = 
    #     sec_h = 


    #     pass

        # sec_h = max



# l2 = [l2 for l2 in l2 if l2 !=l2]
# print(l2)
# for i in l1:
#     if l1 == l2:
#         print(l1)

# print(l2)
# j = 0 
# sec_no = 0 
# h_number = 0

# for i in l1:
    # a1 = max(l1)


    # if i >j:
    #     h_number = i 
    #     j = i
    # # else:
    #     sec_no = j
       

# print(i)
# print(max(l1))
# print(h_number)
# print(sec_n) 


