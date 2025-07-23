# Task 1 : 

#Given an integer, n, perform the following conditional actions:


# If  n is odd, print Weird
# If  n is even and in the inclusive range of  2 to 5 , print Not Weird
# If  n is even and in the inclusive range of  6 to 20  , print Weird
# If  n is even and greater than 20  , print Not Weird

# import math
# import os
# import random
# import re
# import sys

# inclusive range formula == 1 <= n <= 100
# for even numbers and odd == n % 2 == 0 and n % 2 !=0 

# if __name__ == '__main__':

#     print("numbers should be 1 till 100 \n")

#     n = int(input("pick a number:\n").strip())
# if 1 <= n <= 100:# for inlusive range in numbers should be in 1 to 100 
#     if n % 2 == 0 and n > 20 : # for even function and if n is greater than 20 :

#         print("not wierd  its even but greater than 20 ")

#     elif n % 2 != 0 :#for odd numbers 

#         print("wierd its odd number ")

#     elif n % 2 == 0 and 2 <= n <= 5:# inclusive range formula for 2 to 5 

#         print("not wierd")

#     elif n % 2 == 0 and 6 <= n <= 20:# inclusive range  for range 6 to 20 

#         print("wierd") 
# else:
#     print("limit exceed  ")# funcitons to prevent other inputs rather than given 

#task 2 : 
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
# print(a//b)
# print(a/b)

# task 3 :
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#      print(i ** 2 )


# ------------------------------- Area of circle : -------------------------:
# import math
# import re
# import cmath

# def circle(r):

#     pi = 3.14
#     print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
# # r = int(input("enter the radius"))

# circle(int(input()))

import math
# ---------------fucntion for area of elipse for any two a and b axis --------

# def area_elipse(a,b):
#     print("the area of elipse of given axis is : " + str(math.pi*a*b))

# a = float(input("enter a axis: "))
# b = float(input("enter b axis: "))

# elips = area_elipse(a,b)

# # --------------function for area of circle for any radius--------------

# def area_circle(r):
#     """a function to tell the area of circle through give radius 
#     that is taken as input """

#     print("the area of circle of given  is : " + str(math.pi*r**2))

# r = float(input("enter radius : \n "))

# elips = area_circle(r)

# ----------newton law of gravitation: --------

# def law_of_gravitation(m1,m2,r):

#     # variables assigning values formula and constant 
#     G = (6.6743*10**-11)
#     F = (G*m1*m2/r**2)
#     #print statement :
#     print("the newton law of gravitation of given values is  : " + str(F))

# # taking input for mass 1, mass 2 , radius :
# r = float(input("enter radius : \n "))
# m1 = float(input("enter mass 1  : \n "))
# m2 = float(input(" enter mass 2  : \n "))

# elips = law_of_gravitation(m1,m2,r)

# task 4 : make a function for checking input is leap year or not : 

# def is_leap(year):
#     leap = False
    
#     #check if the year is divisible by 4 : 
#     if year % 4 == 0 :
#         leap = True

#     # check if the year is divisble by 100 , and also divisble by 400 if its not leap year  : 
#     if year % 100 == 0 :
#         if year % 400 != 0:
#              leap = False
#     # Write your logic here
    
#     return leap
 
# year = int(input("enter year number : "))
# a = is_leap(year)
# print(a)





# task 5: to make function for entering input number any and show its integer list from 1 to input witout spaces ;
if __name__ == '__main__':
    n = int(input("enter your number : "))
    def function(n):
        for i in range(1,n+1):  # range syntax : range(start, stop , step):
            print(i,end="") # end is use to join are print input as without spaces 
                

function(n)
    # a = function(n)
    # print(a)