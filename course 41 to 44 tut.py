# tut 41 : *args and **kwargs In Python:

#*args specifies the number of non-keyworded arguments
#  that can be passed and the operations that can be 
# performed on the function in Python whereas **kwargs is a
# variable number of keyworded arguments that can be passed to a 
# function that can perform dictionary operations.

# def funarg(normal, *args, **kwargs):
#     print(normal)
#     for item in args:
#         print(item)
#     print("\nthese are our future heroes :\n")
#     for i , j in kwargs.items():
#         print(f"{i} is a {j}")# f strings usage in print code functions :



# normal = "this is a normal argument line now below are the student: \n "
# arg = ["harry", "rohan", "hammad", "rahul","malik", "dj walal ", "carry minati "]
# karg = {"Rahul":"Cook", "Deevan":"programmer", "Ali":"Artist", "Junaid":"designer"}

# funarg(normal, *arg, **karg)

# tut 42 : Time Module In Python:

# import time # this is how u import time module in python 
# seconds_while = time.time()# time.time function is to tell the tics or u can say seconds in result or outputs 
# k = 0 
# while (k<897):
#     print("this is the line same in while loop ")
#     k += 1 # or u can wrtie also k = k + 1
# print(f"while loop ran in, {time.time() - seconds_while} : seconds ")

# seconds_for = time.time()
# for i in range(897):
#     print("this is a length of line in range 45 times in  output ")
# print(f"for  loop ran in, {time.time() - seconds_while} : seconds ")# f srtings usage ;

# local_time = time.asctime(time.localtime(time.time()))# this will print the local time in result output 
# time.sleep(5)#time. sleep function is to stop the command in your preferred seconds and it will run after that.
# print(local_time)

#tut 43 : Virtual Environment & Requirements.txt: )

#tut 44 : enumerate functions : 
#enumerate : mention a number one by one sequence  :


# x = enumerate(var)
# print(f"the accurance of 1 is :{var.count(1)}")
# print(f"the accurance of 2 is :{var.count(2)}")
# print(f"the accurance of 3 is :{var.count(3)}")
# print(f"the accurance of 4 is :{var.count(4)}")
# print(f"the accurance of 5 is :{var.count(5)}")
# print(f"the accurance of 6 is :{var.count(6)}")
# print(f"the accurance of 7 is :{var.count(7)}")
# print(f"the accurance of 8 is :{var.count(8)}")
# print(f"the accurance of 9 is :{var.count(9)}")

# for index, item in enumerate(var):
#       print(index, item)
      

# print(list(x))/

# y_list = ['a', 'b', 'c']

# for index , item in enumerate (y_list):# u can determine where u start from 
#     print(index, item)


# list = [ "a", "b", "j"]
# for index , item in enumerate(list):
    # print(index, item)
# for index, character in enumerate("hello"):
    # print(index, character) 

# count = {}
# indices = {}
# list = [ 1,2,4,5,6,3,3,3,5,2,6,7,87,8,8,9,5,5]

# for index , value in enumerate(list):
#     if value in count.keys():
#         count[value] += 1 
#         indices[value].append(index)
#     else:
#         count[value] = 0 
#         indices[value] = []

# seperator = " , "
# for value , count_value in count.items():
#     print(f"{value} is repeated : {count_value} times and indices are {seperator.join(map(str , indices[value]))} ")








# count = {}
# indexs = {}
# my_dict =[1,2,3,4,1,6,2,5,3,9,8,7,6,2]
# for index, value in enumerate(my_dict): 
#     if value in count:
#         count[value] += 1 
#         indexs[value] += 1
       
#     else:

#         count[value]= 0
#         indexs[value] = count
# for index , value in count.items():
    # print(f"{index} is repeated : {value} times in :  {index} ")



# count = {}
# list1 = [2,3,4,5,3,2,3,5,4,5,4,2,1,3,2,]

# for index , value in enumerate(list1):
#     if value in count.keys():
#         count[value] += 1 
    
#     else:
#         count[value] = 0 

# for index , value in count.items():
#     print(f"{index} is repeated : {value} times ")


# count = {}
# indices={}
# list1 = [2,3,4,5,3,2,3,5,4,5,4,2,1,3,2]

# for index , value in enumerate(list1):
#     if value in count.keys():
#         count[value] += 1
#         indices[value].append(index) 
        

#     else:

#         count[value] = 0 
#         indices[value] = []


# for value , count_value in count.items():
#     print(f"{value} is repeated : {count_value} times  index numbers are { ' , '.join(map(str, indices[value]))}")
# #iska implement karna 

# for index, value in enumerate(list1):
    # print(f" and these are the indexes {index}")
#     if value in indices.keys():
#         indices[value] = index

#     else:
#         indices[value] = index
        
# for index , value in indices.items():
    



# psd = {}
# dsd = [2,4,3,3]
# for index , value  in enumerate(dsd):
#     print(index)
#     if value in psd.keys():
#         psd[value] += 1 

#     else:
#         psd[value] = 0 

# # for index, value in psd.items():
# #     print(f" {index} is {value} ")


# learn ("join funtion ()") , (map function()) , (filler) , (lamda):-----------------------

#join function():-----------------------------------
# tuple2 = ("harry", "ali", 2)
# tuple3 = ("malik", "shahbaz ", "rohan "), ','.join(map(str, tuple2))
# it will work for string but in case of integer u will need to convert it by .join(map(str, tuple2))

# list2 = ["3", "5", "4"]#iterable should be string if not it will throw error 
# seprator = '> '
# print("list before using join() :" , list2)
# print("list after using the join()" , seprator.join(list2)) 
# # print(tuple3)
# list3 = ["jhon", "cena " , "randy ", "orton ", "khali ", "sheamus"]

# a = " , ".join(list3)
# print(a)

# dict1 = {"harry":"comma", "udhar": "ghaat"}#its only joins the key of dictionary in join functions 

# sepratorr = " , bubble , ".join(map(str, dict1.items()))

# print(sepratorr)

# dict3 = {"harry":"phd", "carry":"minati", " ducky": "bhai"}
#
# print("this is dict ", " and ".join(map(str, dict3.items())))# to print all the values of dictionary in python join functions :


# now learning Map functions: ----------------------------

# map in python is a functions that works as an iterator
#  to retrun a result after applying a functions to every item of an iterable .

# Syntax : map(fun, iter)

# square functions use of map : 
# def square(a):
#     return a * a

# numbers = [2, 4, 6, 8, 9]
# # map2 = list(map(square, numbers))# use list to typecast the result as strings 
# # print(map2) # thats how map funcitons are use they typecast the value directly and map the value in your need : 
# map2 =  map(lambda x:x*x , numbers)
# print(list(map2))  

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

# ---------------------- filter functions --------------------------------------:

#Python's filter() is a built-in function that allows you to process an iterable and extract 
#those items that satisfy a given condition. This process is commonly known as a filtering operation.

# function that filter num > 5 values : 

# lsit1 = [23,45,6,4534,35,34,54,53,434,54,6,5,4,2,4]

# def greater_5(num):
#     return num>5 

# list2 = list(filter(greater_5, lsit1))
# print(list2)

# lst = [1 , 3, 3,4,5,5,4,5,4]

# def function(num):
#     return num<5 

# filter1 = filter(function, lst)
# print(list(filter1))


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

# def function(n):
#     numbers = [ 2, 2 , 2, 4,3]
#     if n in numbers:
#         return True
#     else:
#         return False

# new_numbers = [3, 2, 2, 4, 5]
# fliterd = filter(function, new_numbers)
# print(list(fliterd))

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
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# filtered = filter(is_multiple_of_3,numbers)
# print(list(filtered))
 
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

# # ------------------- os modules --------------

import os 

# cwd = os.getcwd()

# print(cwd)


# #cwd = (current working directory )means where python is currently processing

# # to create a new file os.chdir() method is used 

# # os.path.join()--------------:

# # Python program to explain os.path.join() method

# path = "\home"
# # #path 

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
# path component is empty
# so a directory separator ('/')
# will be put at the end
# along with the concatenated value













