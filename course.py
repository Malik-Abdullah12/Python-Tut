#45 how to imports work in python : 

# import sys 
# print(sys.path)

# import file
# print(file.a)
# file.joke(": dont mind ")

# 46  : If __name__==__main__ usage & necessity:

# def functionst(str):
#     return f"bhai yay hia f string ka use: dekha  {str} "

# def add(num2 , num3):
#     return num2 + num3 + 5 

# if __name__=='__main__':
#     print(functionst("there is the code never lies"))
#     o = add(3, 5 )
#     print(o)


# Firstly, it allows you to separate the executable code from the module definition code. 
# This makes it easier to import and use the module in other programs. Secondly, 
# it can help improve the performance of your Python programs.12-Jun-2023

#48 join functions : 

#join function():-----------------------------------
# tuple2 = ("harry", "ali", "kamran ")
# tuple3 = ("malik", "shahbaz ", "rohan "), ','.join(tuple2)

# list2 = ["3", "5", "4"]#iterable should be string if not it will throw error 
# seprator = '> '
# # print("list before using join() :" , list2)
# # print("list after using the join()" , seprator.join(list2)) 
# # print(tuple3)
# list3 = ["jhon", "cena " , "randy ", "orton ", "khali ", "sheamus"]

# # a = " , ".join(list3)
# print(a)

# dict1 = {"harry":"comma", "udhar": "ghaat"}#its only joins the key of dictionary in join functions 

# sepratorr = " ,bubble, ".join(dict1)

# print(sepratorr)

# dict3 = {"harry":"phd", "carry":"minati", " ducky": "bhai"}
#
# print("this is dict ", " and ".join(map(str, dict3.items())))# to print all the values of dictionary in python join functions :


#49 map filter and reduce :-------------------------------------------------
#------------------------reduce ---------------------------------------------
# from  functools import reduce 
# lsit1  = [2, 24, 5 , 4 , 5 ,4]

# num = reduce(lambda x,y:x*y, lsit1)

# print("the sum of all list at once its :", num, " \n hahaha its actually multiply ")

#--------------------------------map---------------------

# now learning Map functions: ----------------------------

# map in python is a functions that works as an iterator
#  to retrun a result after applying a functions to every item of an iterable .

# square functions use of map : 
# def square(a):
#     return a * a 

# numbers = [2, 4, 6, 8, 9]
# map2 = list(map(square, numbers))# use list to typecast the result as strings 
# # print(map2) # thats how map funcitons are use they typecast the value directly and map the value in your need : 

# # use of lambda by map : 
# number = [3, 5, 7, 9, 11]
# map3 = list(map(lambda x: x * x , number))# can also use lambda functions for its use 
# # print(map3)

# # adding two lists using map and lambda 
# numbers2 = [2, 4, 6, 8, 9]
# number = [3, 5, 7, 9, 11]
# map4 = list(map(lambda x,y : x + y , number,numbers2 ))# can also use lambda functions for its use 
# # print(map4)

# #list of strings 

# l = ["sar", "car", "tar", "par", "var"]

# operation  = list(map(list, l ))
# # print(operation)

# another functions using map and lambda and functions : 


# def sqr(a):
#     return a * a 

# def cub(a):
#     return a * a * a



# functions = [sqr,cub]

# for i in range(5):
#     func = list(map(lambda x: x(i), functions))
#     print(func) #  dont print this outside for loop it will not work obv then :


# filter : here is the code practice of filter : 

# ---------------------- filter functions --------------------------------------:

#Python's filter() is a built-in function that allows you to process an iterable and extract 
#those items that satisfy a given condition. This process is commonly known as a filtering operation.

#function that filter num > 5 values : 
# lsit1 = [23,45,6,4534,35,34,54,53,434,54,6,5,4,2,4]

# def greater_5(num):
#     return num>5 

# list2 = list(filter(greater_5, lsit1))
# # print(list2)

# # function that filters vowels : 

# def function2(a):
#     vowels = ["a", "e", "i", "o", "u"]
#     if (a in vowels):
#         return True
#     else:
#         return False
    
# alphabet2 = ["a", "i", "g","l", "k", "q", "y", "e" ]

# filtered = list(filter(function2,alphabet2))
# print(filtered)
#------------or ----------------------
# filtered = list(filter(function2,alphabet2))
# print("below is the result:")
# # for i in filtered:# can use this method to 
    # print(i)

# print(filtered)# or if you want to print direct then u will have to typecast in to the list.

#-------------# a list contains both even and odd numbers.

# seq = [2,3,5,2,6,7,65,3,3,5,6,7]

# result = list(filter(lambda x : x % 2 != 0 , seq))
# print(result)

# result2 = list(filter(lambda x : x % 2 == 0 , seq))
# print(result2)

# # ------------ define a function to check if a number is a multiple of 3 : 


# def is_multiple_of_3(num):
#     return num % 3 == 0
 
 
# # Create a list of numbers to filter
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
 
# Use filter and a lambda function to
# filter the list of numbers and only
# keep the ones that are multiples of 3
# result = list(filter(lambda x: is_multiple_of_3(x), numbers))
 
# Print the result
# print(result)


# ----------------a function of which tells greater number than 11 and and gives the squares of given numbers ;

# def greater(a):
#     if a > 11 :
#         return True
#     else:
#         return False

# numbers = [2,4,5,6,5,65,3,45,45]
# greaters = list(filter(greater,numbers))
# print( "these are the greater number than 11 in the list: \n ", greaters,"\n")

# print("now below are the squares of numbers of list: \n  ")

# x = lambda x: x*x
# y = list(map(x,numbers))
# print(y)

# -----------------------------------os.path.join method --------------------------

# ------------------- os modules --------------

# import os 

# cwd = os.getcwd()

# print(cwd)


# #cwd = (current working directory )means where python is currently processing

# # to create a new file os.chdir() method is used 

# # os.path.join()--------------:

# # Python program to explain os.path.join() method

# path = "\home"
# #path 

# print(os.path.join(path, "\downloads" , "course.py"))


# path = "user\Documents"

# print(os.path.join(path, "\home" , "documents"))

# # In above example '/home'
# # represents an absolute path
# # so all previous components i.e User / Documents
# # are thrown away and joining continues
# # from the absolute path component i.e / home.
 

# path = "/User"
 
# # Join various path components
# print(os.path.join(path, "Downloads", "file.txt", "/home"))
 
# # In above example '/User' and '/home'
# # both represents an absolute path
# # but '/home' is the last value
# # so all previous components before '/home'
# # will be discarded and joining will
# # continue from '/home'

# path = "/home"
 
# # Join various path components
# print(os.path.join(path, "User/Public/", "Documents", ""))
 
# # In above example the last
# # path component is empty
# # so a directory separator ('/')
# # will be put at the end
# # along with the concatenated value

# -------------------------------------------------REG EX :-------------------------------------------------

# A Regular Expressions (RegEx) is a special sequence of characters that uses a search 

# pattern to find a string or set of strings. It can detect the presence or absence of a 

# text by matching it with a particular pattern, and also can split a pattern into one or 

# more sub-patterns. Python provides a re module that supports the use of regex in Python. 

# Its primary function is to offer a search, where it takes a regular expression and a string. 

# Here, it either returns the first match or else none.

import re 

# s = " geeeks : for geeks is a programing language course website its good portal"

# match = re.search(r"portal",s) 
# # Here r character (r’portal’) stands for raw, not regex. The raw string is slightly different 
# # from a regular string, it won’t interpret the \ character as an escape character. This is because 
# # the regular expression engine uses \ character for its own escaping purpose.

# print("start index: "  , match.start())
# print("end  index: "  , match.end())

#To understand the RE analogy, MetaCharacters are useful, 
# important, and will be used in functions of module re. Below is the 
# list of metacharacters.

#--------------Meta Characters: ------------------

# \

# Used to drop the special meaning of character following it

# []

# Represent a character class

# ^

# Matches the beginning

# $

# Matches the end

# .

# Matches any character except newline

# |

# Means OR (Matches with any of the characters separated by it.

# ?

# Matches zero or one occurrence

# *

# Any number of occurrences (including 0 occurrences)

# +

# One or more occurrences

# {}

# Indicate the number of occurrences of a preceding regex to match.

# ()

# Enclose a group of Regex


#-----------using backslash -----------

#The backslash (\) makes sure that the character
#  
# is not treated in a special way. 

# d = "intellectual.geekk.sdf"

# # without the backslash 
# match = re.search(r".", d )
# print(match)

# # with the backslash 
# match = re.search(r"\.", d )
# print(match)

# ----------square brackets :[]---------:

#square Brackets ([]) represent a character class consisting of a set 

# of characters that we wish to match. For example, the character class

#  [abc] will match any single a, b, or c. 

# We can also specify a range of characters using – inside the square brackets. For example, 

# srt = "the quick little brown fox jumps over the lazy dog "

# pattern = "[a-z]"
# match  = re.findall(pattern, srt)

# print(match)

#----------------------- Caret ^-------------------------:

# Caret (^) symbol matches the beginning of the string i.e. checks whether the string

#  starts with the given character(s) or not. For example –  

# ^g will check if the string starts with g such as geeks, globe, girl, g, etc.

# ^ge will check if the string starts with ge such as geeks, geeksforgeeks, etc.

# regex = r"^randy"

# string = ["randy orton ", "randy bliss", "randy bluke", "jhon cena"]

# for s in string:
#     if re.match(regex , s):
#         print(f"yes its a match: {s}")
    
#     else:
#         print(f"not its not a match: {s} " )


# ------------------Dollar $ -------------:

#Dollar($) symbol matches the end of the string i.e checks whether the string ends 

# with the given character(s) or not. For example – 

# s$ will check for the string that ends with a such as geeks, ends, s, etc.

# ks$ will check for the string that ends with ks such as geeks, geeksforgeeks, ks, etc.


# import re
 
# string = "Hello World!"
# pattern = r"World!$"
 
# match = re.search(pattern, string)
# if match:
#     print("Match found!")
# else:
#     print("Match not found.")

# -----------------Dot . -----------------:

# Dot(.) symbol matches only a single character except for the newline character (\n). For example –  

# a.b will check for the string that contains any character at the place of the dot such as acb, acbd, abbb, etc
# .. will check if the string contains at least 2 characters

# import re

# string = "The quick brown fox jumps over the lazy dog."
# pattern = r"jumps.over"

# match = re.search(pattern, string)
# if match:
# 	print("Match found!")
# else:
# 	print("Match not found.")


# _________---------------------Or | ----------

# Or symbol works as the or operator meaning it checks whether the pattern before 

# or after the or symbol is present in the string or not. For example –  

# a|b will match any string that contains a or b such as acd, bcd, abcd, etc.

# txt = "The rain in Spain  occurrs mainly in the plain!"

# #Check if the string contains either "falls" or "stays":

# x = re.findall("occurrs|not", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")

# ------------------- question mark ? --------;

# The question mark (?) is a quantifier in regular expressions that indicates that the 

# preceding element should be matched zero or one time. It allows you to specify that 

# the element is optional, meaning it may occur once or not at all. For example,

# ab?c will be matched for the string ac, acb, dabc but will not be matched for abbc because 

# there are two b. Similarly, it will not be matched for abdc because b is not followed by c.
# 
# text = "color or colour?"
# pattern = r"colou?r"

# matches = re.findall(pattern, text)

# for match in matches:
#     print(f"found match : {match}")

# # In this example, the pattern colou?r matches both "color" and
# #  "colour" in the given text because the u? part makes the "u" character 
# optional. The output would be:

# ------------------star * : =---------------:
#
# Star (*) symbol matches zero or more occurrences of the regex preceding the * symbol. For example –  

# ab*c will be matched for the string ac, abc, abbbc, dabc, etc. but will not be matched 
# for abdc because b is not followed by c.

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

# x = re.findall("he.*o", txt)

# print(x)

#-----------------plus + ---------:

# Plus (+) symbol matches one or more occurrences of the regex preceding the + symbol. For example –  

# ab+c will be matched for the string abc, abbc, dabc, but will not be matched for ac, abdc, because 

# there is no b in ac and b, is not followed by c in abdc.

# txt = "heo planet"

# #Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":

# x = re.findall("he+o", txt)

# print(x)

# ------------braces -  {m, n}: ------------:

# Braces match any repetitions preceding regex from m to n both inclusive. For example –  

# a{2, 4} will be matched for the string aaab, baaaac, gaad, but will 

# not be matched for strings like abc, bc because there is only one a or no a in both the cases. 

# txt = "hello planet"

# #Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":

# x = re.findall("he.{2}o", txt)

# print(x)

# -------findall functions----------- : 

#The findall() function returns a list containing all matches.

# text = "the spain is in rain where ever it gets pain tain gain"

# imp = re.findall("ai", text)

# print(imp)

# # for i in imp:
# #     print(i)
# #     if i:
# #         print("yes its true ")
# #     else:
# #         print("not found ")

# --------------The search() Function-----:

#The search() function searches the string for a match, and returns a Match object if there is a match.

# If there is more than one match, only the first occurrence of the match will be returned:

# txt = "The rain in Spain"
# x = re.search("\s", txt)

# print("The first white-space character is located in position:", x.start())

# ------------ the split fucntions : ----

#he split() function returns a list where the string has been split at each match:

# for white spaces :

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)

# # for implementation in strings :
# txt = "The rain in Spain"
# y = re.split("ai", txt)
# print(y)

# #------ the sub functions();_---------------------:

#he sub() function replaces the matches with the text of your choice:

# txt = "the sub functions work well"

# x = re.sub("sub","dub", txt)

# print(x)

# #Replace the first two occurrences of a white-space character with the digit 9:

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt, 2)
# print(x)

# # -------
# txt = "the sub dub kub well"

# x = re.sub("ub","bu", txt,1)

# print(x)

# # ---------- Match Object ---------:

# # A Match Object is an object containing information about the search and the result.

# #The search() function returns a Match object:

# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x)

# The Match object has properties and methods used to retrieve information about the search, and the result:

# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match


# .span() returns a tuple containing the start-, and end positions of the match;

# sdt = "I Am Singing a piano"

# sxt = re.search(r"\bS\w+", sdt)
# print(sxt.span())

# # .string ;
# sdt = "I Am Singing a piano"

# sxt = re.search(r"\bS\w+", sdt)
# print(sxt.string)

# # group():

# txt = "The rain in  in the Sain"
# x = re.search(r"\bS\w+", txt)
# print(x.group())

# ------------backslashes ________------"";

# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	

# \b	Returns a match where the specified characters are at the beginning or at the end of a word

# ((the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"	)

# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"	

# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	

# \D	Returns a match where the string DOES NOT contain digits	"\D"	

# \s	Returns a match where the string contains a white space character	"\s"	

# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	

# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"
# 	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	

# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	
#----------------------

 # ------------------sets : -------------------

# [arn]	Returns a match where one of the specified characters (a, r, or n) is present	

# [a-n]	Returns a match for any lower case character, alphabetically between a and n	

# [^arn]	Returns a match for any character EXCEPT a, r, and n	

# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	

# [0-9]	Returns a match for any digit between 0 and 9	

# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	

# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	

# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string	

#--------------------------------------x---------------:

# re.findall another use : 

# string = """Hello my Number is 123456789 and
#             my friend's number is 987654321"""
 
# # A sample regular expression to find digits.
# regex = '\d+'
 
# match = re.findall(regex, string)
# print(match)

#  ------------------------------------re.compile :----------------

# p = re.compile("[a-e]")

# print(p.findall("said to be there at the moment "))

# # ------
# # \d is equivalent to [0-9].
# p = re.compile('\d')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))
 
# # \d+ will match a group on [0-9], group 
# # of one or greater size
# p = re.compile('\d+')
# print(p.findall("I went to him at 11 A.M. on 4th July 1886"))

# -------------------------decorators in python : tut 51 : -------------------

# def func():
#     print("state")
# func2 = func
# del func
# func2()# func2 will work because it has already made its copy from func

# def funcret(sum):
#     if sum== 0 : 
#         return True
#     if sum==1:
#         return False

# # a = funcret(int(input("enter the number : ")))
# # print(a)

# def sef(fun):
#     fun("print")
# sef(print)

# def dec1(fus):
#     def dec2():
#         print("executing now-------- ")
#         fus()
#         print("executed!")
#     return dec2
    
# @dec1 # decoraters : 
# def haris():
#     print("haris is a good boy ")

# haris()



#  __________________-----------------num py module: --------------:

# NumPy is a Python library used for working with arrays.

# It also has functions for working in domain of linear algebra, fourier transform, and matrices.

# NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.

# NumPy stands for Numerical Python.

# why use python: 

# In Python we have lists that serve the purpose of arrays, but they are slow to process.

# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

# The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

# Arrays are very frequently used in data science, where speed and resources are very important.



import numpy as np  # we can set alias name : 

# # numpy array list :

# dnarray = np.array([1,2,3,4,5,6])# numpy list :

# print("\nthis is numpy list array : \n ")
# print(dnarray , "\n ")

# # to check numpy version : 

# print("num py version :", np.__version__ , "\n") # for finding out the version of your numpy 

# #normal array list : 
# array = [1,2,34,5]# a normal list : 
# print("this is a normal list see the diffrence : \n ")
# print(array , "\n ")

# ---------------creating arrays (): ----------:

# NumPy is used to work with arrays. The array object in NumPy is called ndarray.

# We can create a NumPy ndarray object by using the array() function.

# arr = np.array([1,21,3,4,5,6,7])

# print("\n",arr, "\n")
# print(type(arr))

# To create an ndarray, we can pass a list, tuple or any array-like object into
 
# the array() method, and it will be converted into an ndarray:

# ar = np.array((1,21,3,4,5,6,7)) # tupple form array also will be converted in to ndarray form 

# print("\n",arr, "\n")

#A dimension in arrays is one level of array depth (nested arrays).

# nested array: are arrays that have arrays as their elements.

# 0-D arrays : ----------------- 

# d0 = np.array(42)

# print(d0)

# 1-d Arrays : -------------

# A dimension in arrays is one level of array depth (nested arrays).

# nested array: are arrays that have arrays as their elements.

# d1 = np.array([1,2,3,4,5])

# print(d1)

# # 2-d Arrays : -------------

# d2 = np.array([[1,2,3],[4,5,6]])

# print(d2)

# 3-d Arrays : -------------

# An array that has 2-D arrays (matrices) as its elements is called 3-D array.

# These are often used to represent a 3rd order tensor.

# d3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

# print(d3)

# Check Number of Dimensions?

# NumPy Arrays provides the ndim attribute that returns an integer that 

# tells us how many dimensions the array have.
# d0 = np.array(42)
# d1 = np.array([1,2,3,4,5])
# d2 = np.array([[1,2,3],[4,5,6]])
# d3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

# print(d0, "dimesions number:" , d0.ndim) # to check the number of dimensions : 
# print(d1, "dimesions number:" , d1.ndim)
# print(d2, "dimesions number:" , d2.ndim)
# print(d3, "dimesions number:" , d3.ndim)

# to change the dimensions of ones arrays : --------

# When the array is created, you can define the number of dimensions by using the ndmin argument.

# arr = np.array([1, 2, 3, 4], ndmin=2) 
# print(arr)

# ab = np.array([1,2,3,5], ndmin=5)
# print(ab , "number of dimension " , ab.ndim)

# ----------------------NumPy Array Indexing------------:

# Access Array Elements

# Array indexing is the same as accessing an array element.

# You can access an array element by referring to its index number.

# The indexes in NumPy arrays start with 0, meaning that the first element has index 0, and the second has index 1 etc.

# array indexing : 
# var = np.array([2,3,45,3,4])

# print(var[2])

# get more than one index : 

# var2 = np.array([2,3,45,3,4])

# print(var2[2], var2[4])

# Get third and fourth elements from the following array and add them.

# var3 = np.array([2,3,45,3,4])

# print(var3[2] + var3[4]) 
    
# To access elements from 2-D arrays we can use comma separated 

# integers representing the dimension and the index of the element.

# Think of 2-D arrays like a table with rows and columns, where the
#  dimension represents the row and the index represents the column.

# var24 = np.array([[2,3,56,354,34],[2,34,5,34,24]])

# print("first row second column is  : ",var24[0,1])

# Access the element on the 2nd row, 5th column:

# var24 = np.array([[2,3,56,354,34],[2,34,5,34,24]])

# print("second row 5th  column is  : ",var24[1,4])

# -----------------Access 3-D Arrays------:

# To access elements from 3-D arrays we can use comma separated integers
#  representing the dimensions and the index of the element.

# var23 = np.array([[[2,3,77,354,34],[2,34,78,34,24]],[[2,3,56,4334,34],[2,34,5,45,56]]])

# print("the value should be 78 : ",var23[0,1,2])

# Negative Indexing: -----------
# Use negative indexing to access an array from the end.

# operation on first row : 
# var21 = np.array([[2,3,56,354,34],[2,34,5,34,24]])
# print(var21[1,-1]) # second row last column because negative sign 

# operation on second row : 
# var20 = np.array([[2,3,56,354,34],[2,34,5,34,24]])
#  print(var20[0,-1]) first row last column because negative sign 


# --------------------------NumPy Array Slicing-----------:

# Slicing arrays
# Slicing in python means taking elements from one given index to another given index.

# We pass slice instead of index like this: [start:end].

# We can also define the step, like this: [start:end:step].

# If we don't pass start its considered 0

# If we don't pass end its considered length of array in that dimension

# If we don't pass step its considered 1

# arr = np.array([1,2,3,4,5,6])

# print("sliciing from 1 to 5  :",arr[1:5]) # The result includes the start index, but excludes the end index

# #Slice elements from index 4 to the end of the array:
# arr2 = np.array([1,2,3,4,5,6,7,8,9,10,11])
# print("slicing from 4 to end : ",arr2[4:])# If we don't pass end its considered length of array in that dimension

# arr3 = np.array([1,2,3,4,5,6,7,8,9,10,11])
# print(" slicing form 0 to 4  :", arr3[:4]) # Slice elements from the beginning to index 4 (not included):

# Negative Slicing--------
# Use the minus operator to refer to an index from the end:


# End Index: The -end_index specifies the starting point for the slice, counting from the 
# end of the array. It refers to the element that will be included in the slice. -1 represents
#  the last element, -2 represents the second-to-last element, and so on.

# Start Index: The -start_index specifies the ending point for the slice, 
# counting from the end of the array. It refers to the element that will not
#  be included in the slice. -1 represents the last element, -2 represents the second-to-last element, and so on.

# Slicing Direction: The slice goes from the element specified by -end_index 
# to the element just before -start_index. The result includes the element at -end_index and
#  excludes the element at -start_index.

# ab = np.array([1,2,4,3,5,3,9])
# print(ab[-6:-2])

# --------Step--------():

# In slicing, the step is an optional parameter that controls the increment between elements in the slice.
#  It allows you to skip elements when slicing an array or sequence.
#  The step is specified using the colon : as part of the slicing syntax. Here's the general syntax:


# start:stop:step
# start: The index at which the slice begins.
# stop: The index at which the slice ends (not inclusive).
# step: The step or increment to skip elements.
# By default, if you omit the step in slicing, it is assumed to be 1, which means that you include every element 
# from the start to the end. However, you can use the step to skip elements by specifying a value other than 1.

#Return every other element from index 1 to index 5:
# arr = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr[1:5:2])

# #Return every other element from the entire array:
# arr2 = np.array([1, 2, 3, 4, 5, 6, 7])

# print(arr2[::2])

# examples of simple slicing :------
# my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # Slicing with a step of 2, which selects every other element
# result1 = my_list[0:10:2]
# print("slicing with a step of 2 :",result1)

# # Result: [0, 2, 4, 6, 8]

# # Slicing with a negative step, which reverses the order
# result2 = my_list[::-1]
# print("this method reverse the order :",result2)

# # Result: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# # Slicing with a step of 3 starting from index 2
# result3 = my_list[2::3]
# print("slicing with a step of 3: ",result3)
# # Result: [2, 5, 8]

# result4 = my_list[::2]
# print("this is result 4 ", result4)



# Slicing 2-D Arrays---------

# , is used to separate the row and column selections.

# variable1 = np.array([[2,3,4,5,6,7], [8,9,10,11,12,13]])
# print("From the second element, slice elements from index 1 to index 4 (not included):",variable1[1, 1:4])
# #Remember that second element has index 1.

# variable2 = np.array([[2,3,4,5,6,7], [8,9,10,11,12,13]])
# print("to call all index : ", variable2[0:2])


# variable3 = np.array([[2,3,4,5,6,7], [8,9,10,11,12,13]])
# print("From the first  element, slice elements from index 1 to index 4 (not included): ", variable3[0, 1:4])


# variable4 = np.array([[2,3,4,5,6,7], [8,9,10,11,12,13]])
# print("slicing index 4 , column 3rd from both the indexes :",variable4[0:2, 4])
# #, is used to separate the row and column selections.

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:

# variable5 = np.array([[2,3,4,5,6,7], [8,9,10,11,12,13]])
# print(variable5[0:2, 1:4])

