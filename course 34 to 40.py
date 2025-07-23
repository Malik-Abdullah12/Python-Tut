# #34 recursion : recusive vs iterative/

# # n! = n * n-1 * n-2 * n-3.......1
# # n! = n * (n-1)!



# def factorial_iterative(n):
#     """
#         :param n: Integer
#         :return: n * n-1 * n-2 * n-3.......1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac

# def factorial_recursive(n):
#     """
#         :param n: Integer
#         :return: n * n-1 * n-2 * n-3.......1
#     """
#     if n ==1:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
#     # 5 * factorial_recursive(4)
#     # 5 * 4 * factorial_recursive(3)
#     # 5 * 4 * 3 * factorial_recursive(2)
#     # 5 * 4 * 3 * 2 * factorial_recursive(1)
#     # 5 * 4 * 3 * 2 * 1 = 120

# # 0 1 1 2 3 5 8 13
# def fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+ fibonacci(n-2)


# number = int(input("Enter then number"))
# # print("Factorial Using Iterative Method", factorial_iterative(number))
# # print("Factorial Using Recursive Method", factorial_recursive(number))
# print(fibonacci(number))
  
#35 : answer of exercize 4 


#36: Anonymous/Lambda Functions In Python;


# Lambda functions or anonymous functions
# def add(a, b):
#     return a+b
#
# # minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))
# p = lambda x,y : x-y
# print(p(9,4))

# a =[[1, 14], [5, 6], [8,23]]
# a.sort(key=lambda a:a[1])
# # print(a)

# x = lambda a, b : a * b
# print(x(5, 6))
#  #u can also summarize arguments
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))



# practice work:

# def add(a,b):
#     return a + b 
# print(add(2,34))


# p1 = int(input("enter your number "))
# p2 = int(input("enter your number "))
# def function1(n,m):
#     for i in range(1,p1+p2 + 1):
#         print(i)


# print(function1(p1,p2))
# def sum_of(n):
#  total=0
#  for i in range(1,n+1):
#   total = total + i 
#  return total
  
# inputt = int(input("enter a value for n: "))
# print("Sum: ",sum_of(inputt))


#37 exercize 5 solution and answer :

#38 : Using Python External & Built In Modules:

#module is just like a library of coding where you can use  commands or function in it

# # random modules in python and its function
# import random
# random_number = random.randint(1,56)
# # print(random_number)

# rand = random.random() * 100
# # print(rand) 

# lst = ["Marvel", "DC", "Sony", "Experia", "HBO", "Netflix", "Movie_watch"]
# choice = random.choice(lst)
# # print(choice)


# mylist = ["apple", "banana", "cherry"]

# # print(random.choices(mylist, weights = [10, 1, 1], k = 10))#weights represnet the value of greatness of number
# # k is representing integer data 

# # statistics module and its built in function . 
# import statistics
# lst1 = [23,54,54,54,3,23,5646,54,34,23,5,4,645,45,23,23,5,6,7,5,54]
# lst2 = [23,5,4,645,45,23,23,5,6,7,5,54]
# lst3 = [23,54,54,54,3,23,5646,54,34,23]

# #calculating average of the given data .
# average = statistics.mean(lst1)
# average2 = statistics.mean(lst2)
# average3 = statistics.mean(lst3)

# # print("this is average of lst1 :", average, "\n")
# # print("this is average of lst2 :",average2 , "\n")
# # print("this is average of lst3 :",average3 , "\n")
# # print("this is the direct method to use the statistics mean function :", statistics.mean([34,435,433,23]) , "\n")

# # calculating middle values :

# lst4 = [2354,3,23,5646,54,34,]
# lst5 = [23,5,4,645,455,54]
# lst6 = [23,54,54,54,3,23]

# age = statistics.median(lst4)
# age2 = statistics.median(lst5)
# age3 = statistics.median(lst6)

# # print("this is middle value of lst4 :", age , "\n")
# # print("this is middle value  of lst5 :", age2 , "\n")
# # print("this is middle value of lst6 :", age3 , "\n")
# # print("this is the direct method to use the statistics median  function :", statistics.median([34,435,433,23]) , "\n")

# # datetime module and its functions 
# import datetime
# x = datetime.datetime.now()
# # print(x)
# print(x.strftime("%c"), "\n ")
# # print(x.strftime("%y"))


# #math module and its two functions :
# import math  
# # function of factorial in math module :
# fac = 5

# # to return factorial of fac 98 
# print("math factorial funciton: \n ")
# print("this is the factorial of fac var :", math.factorial(fac), "\n")
# print("this is the direct way of finding a factorial that is 8 given data : ", math.factorial(8), "\n")

# # function math.exp :
# #The math.exp() method returns E raised to the power of x (Ex).
# exp2 = 23
# exp4 = 23
# exp3 = 23
# print("math exp funciton: \n ")
# print("raise power of x :", math.exp(exp2), "\n")
# print("raise power of x :", math.exp(exp3), "\n")
# print("raise power of x :", math.exp(exp4), "\n")


# #39 f string and f string formatting in python :
# # format method :

# a = "harry"
# c = 43
# ink = f"my name is {a} and i am {c} years old "
# b = ink.format(a,c)
# print(b)

# # F strings :
# import math
# w = "run "
# o = "write "
# p = "different "

# k = f"this is the program to {w} and {o} data in {p} forms,\n this is cos value of 30: {math.cos(30)}"
# print(k)# we can assign any variables in f strings as u can see and u can use any functions in it .

# #40 exercize python water gun snake game in python :

