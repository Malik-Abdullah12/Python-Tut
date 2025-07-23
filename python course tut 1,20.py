# print("hello world")
# print("what a beautifull dayy")
# print("parrot is green")
# #its a comment
# #dont read it 
# # the following above is sytnax
# #this is a code to be not function 
# #and the python should ignore it 
# print("its a valuable data", end=" ,")#from this u can mix two lines of the code in one sequence 
# print("for programming") 
# print("now we are mixing two lines", end=" ,")
# print("the line is mixed as u can see")
# print("next line but now","its on the same page")
# print("if u dont use comma after new line" "it will match the line with no space ")#if u dont use comma after new line" "it will match the line with no space
# print("escape sequence helps us to right our data in special forms")
# print("now we are using sequence \n new line and 2 \t")

# print("now learning variables values string, float, integer")
# var1 = "hello world "#string data , to give space if u are using line in us should left space before quotation
# var2 = 45 #integer data 
# var3 = 34.5 #float data 
# var4 = "there" #string data 
# var5 = "45" #also string 
# var6 = "54"
# var7 = "48"
# var8 = "23"
# print(type (var1)) #python can recognize the types of date 
# print(type (var3))
# print(type (var2))
# print(var2 + var3)
# print(var1 + var4)
# print(10 * var1)
# print(10 * var2)
# print(5 * "between\n") #from this u can print data how many times u want
# print(int(var5) + int(var6)) #if u want to add strings as integer so u can use int function to convert it 

# str()
# int()
# float()

# print(100 * int(var7) + int(var8)) if we * 100 here the answer will be overight 4323,
# to solve this issue we can use typecasting like with the use str() the int function will simply
# + var7 and var8 then it will behave as string and will be multiply by 100 therefore the result will be
# accurate 

# print(10 * str(int(var7) + int(var8)) ) #this is typecasting with string function to * 10 with outuput
# a = int(input("enter your number :"))
# print("you entered :",a)
# #now using functions for user input
# print("enter your number") 
# inpnum = input() # inpnum is variable name 
# print("you enterd ", int(inpnum)*20) # when u use inpnum in input it will behave as string
#if u want to plus 10 in above function u should first convert str() into int() in print.

# p1 = int(input("enter your first number ; "))
# p2 = int(input("enter your second number ; "))
# print("your answer is :",p1+p2)
# s1 = int(input("enter your first number : "))
# s2 = int(input("enter your second  number : "))
# print("your sum of the given number is   : ", s1 + s2  )
"""#a simple calculator for  adding two numbers
print("enter your first number") 
inpnum2 = input()
print("enter your 2nd number")
inpnum3 = input()
print("your answer is", int(inpnum2) + int(inpnum3))"""
#good practice of this code is on "test.py" line no: 144


#now using string slicing
# # srting[start:stop:step]
# mystr = "farhan is a good boy"
# # # print(mystr[5])
# # print(mystr)
# print(mystr[-10:-1])
# # print(mystr[:])
# print(mystr[0:5:2])# this is called string slicing 
# print(mystr[:8])
# print(mystr[0:6])

# # Omitting start or stop:
# print(mystr[0:8])
# print(mystr[0::2])  # skip two characters and typelist the str

# If start is greater than stop, the slice will be empty.
# The default value for step is 1.
# Negative step values reverse the direction of slicing.

# print(mystr[::])
# print(len(mystr))#len function is use to find the lenght of given data or string
# print(mystr[::-1])#a way to revert the data of string

 # now using functions 
# print(mystr.isalnum())#fucniton is use to see if the data is isalnum or not its a type of boolean
# print(mystr.isalpha())#-----------------------------------------------------------------------
# print(mystr.endswith("boy"))#it tells wether the function is ending with given than state it false or true 
# print(mystr.count("o"))#it count the values 
# print(mystr.capitalize())#this fucntion capatalize the program first letter 
# print(mystr.find("good"))#it finds whatever u are trying to find in a  data 
# print(mystr.lower())#converts all the data in lower case 
# print(mystr.upper())#convert all the data in upper cases
# # print(mystr.replace("is", "bad"))#u can use this to replace the function to any thing u like 
# print(mystr.replace("is" , "ullo "))
# txt = "this is not a code its only text"
# x = txt.encode()#encode fucntion returns an encoded version of string
# print(x)
# print(mystr.find("is"))
# print(txt.count("i"))
# x1 = "subject code "
# txt1 = x1.encode()
# print(txt1)

# # now using list and list functions
# list = ["coordenate", "this",'this is', "can do this"]
# shopping_list = ["eggs", "bacon", "milk", "meat", "catfood"]#list of string data types 
# a = int(input("enter the number"))
# print(shopping_list)
# print(shopping_list[0:3])
# print(list[0:2])

# numbers = [12, 34, 35, 65, 45, 323, 67, 4545]
# numbers.sort()#rearrange the numbers if scramble
# numbers.reverse()#reverse the data from left to right
# numbers.insert(2, 3456)#inserts the numbers of your choice in replace of given data 
# numbers.remove(65) #Removes the first item with the specified value
# numbers.pop(0) # pop up the value that u assign 
# numbers.append(45) # insert that number that is given to the end of the data doc
# numbers [1] = 97#u can change the value of list 
# print(numbers)
# print(numbers[::])
# print(numbers[::-1])
#mutable: can change 
#Imutable : cannot change 

# tp = (1, 2, 3, 4)
# #tp [1] = 34# u cannot change the tuppel becasue its imutable 
# print(tp)
# a = 8 
# b = 87
# a, b = b, a #this is to use interchange values from variables 
# print(a,b)

#tut 10 dictionary and its functions 
# dictionary is nothing but key value pairs 

# d1 = {}#dictionary uses curley bracket
# # print(type(d1))
# d1 = {"abdullah":"kurrke", "hosting":"thie chill"}
# d1 ["good job "]  = "sahi hi "

# d2 = {"harry":"burger", "parrot":"greenchili", "subham":"chai_rooti", "aneesha":"gool gapai",
#        "natsha":{"m":"kebab", "p":"rooti", "c":"paratha"}}
# d2 ["ankit"] = "waffels"#u can add dictionary into existing one 
# # d2 [420] = "samosa"
# # del d2[420]
# # d3 = d2.copy()#Returns a copy of the dictionary
# # del d3["harry"]
# d2.update({"nisha":"potato"})#Updates the dictionary with the specified key-value pairs
# d2.update({"pis":"tell"})#Updates the dictionary with the specified key-value pairs
# d1.update({"now":"guess"})#Updates the dictionary with the specified key-value pairs
# d1.update({"oer":"sdsd"})#Updates the dictionary with the specified key-value pairs

# print(d2)
# print(d1)
# print(d1.keys())
# print(d1.values())
# print(d2["subham"])
# print(d2["natsha"])
# print(d2["parrot"])
# print(d2.keys())#Returns a list containing the dictionary's keys
# print(d2.items())#Returns a list containing a tuple for each key value pair"""
# print(d2["harry"])
#tut 11: python exercize 1 apni dictionary 

"""d1 = {"mutable":"the thing that cannot be changed by any means like a constant value of and data",
      "invent":"to create something from own hands from pieces of materials", "district":"a certain platform of an area",
      "collosal":"a huge giantic substance or body"}
print("what word meaning u are looking for ")
ind1 = input()
print(d1[ind1])"""



# Ex 12 sets in python:

# s = set()
# print(type(s)) 
# l = ["harry", "name"]#u can also direct acces the data by variable calling 
# set_from_list = set([1, 2, 3, 4, 5, 6,])#u can use list with set to form set  list
# set_from_list_b = set(l)
# set_from_list.add(9)
# print(set_from_list)
# print(set_from_list_b)
# print(type(set_from_list_b))
# print(len(set_from_list))
# print(set_from_list, set_from_list_b)# u can also print multiple results at once 
# s.add(1)#	Adds an element to the set
# s.add(2)
# s.add(3)
# s.clear()
# s1 = s.intersection({2, 6, 3, 5})#Returns a set, that is the intersection of two or more sets
# print(s)
#functions 
#add()	Adds an element to the set
#clear()	Removes all the elements from the set
#copy()	Returns a copy of the set
#difference()	Returns a set containing the difference between two or more sets
#difference_update()	Removes the items in this set that are also included in another, specified set
#discard()	Remove the specified item
#intersection()	Returns a set, that is the intersection of two or more sets
#intersection_update()	Removes the items in this set that are not present in other, specified set(s)
#isdisjoint()	Returns whether two sets have a intersection or not
#issubset()	Returns whether another set contains this set or not
#issuperset()	Returns whether this set contains another set or not
#pop()	Removes an element from the set
#remove()	Removes the specified element
#symmetric_difference()	Returns a set with the symmetric differences of two sets
#symmetric_difference_update()	inserts the symmetric differences from this set and another
#union()	Return a set containing the union of sets
#update()	Update the set with another set, or any other iterable

#ex 13 if else and elif conditionals in python 

"""n1 = 6
n2 = 54
n3 = int(input())
if n3>n2:
    print("good")
elif n3==n2:
    print("fair")
else:
    print("bad")

l1 = [1, 2, 5, 6, 7]
print(5 in l1)
if 5 in l1:
    print("yes it is true")
print(54 in l1)
if 53 not in l1:
    print("false")"""

#quiz making a program to take input from user his/her age and telling him is he eligible for driving
#mine own idea
"""print("tell us your age so that we can tell if u  are eligible for driving")
age = 18
drive1 = int(input())
if age<drive1<90:
    print("you are eligible for driving")
elif age==drive1:
    print("sorry! u are 18 but, we cannot tell u u have to come in person so that we can test you physically")
else:
    print("sorry u are underage we cannot now allow u to drive")"""

# how its done in tutorial to a selected path numbers
"""print("tell us your age so that we can tell if u  are eligible for driving")
age = int(input())
if 18<age<90:
    print("you are eligible for driving")
elif age==18:
    print("sorry! u are 18 but, we cannot tell u u have to come in person so that we can test you physically")
else:
    print("sorry u are underage we cannot now allow u to drive")"""

# excersize 2: faulty calculator!
# Exercise 2 - Faulty Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except
# the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
"""print("welcome to the best calculator for math test ")
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
        print("enter a valid function to operate")"""

# class 16# "for" loops 

# list1 = ["harry", "carry", "larry", "marry"]
# list2 = [["harry", 23, 78], ["carry", 89, 89], ["larry", 898, 78], ["marry", 98, 85]]
# list3 =  [["harry", 23], ["carry", 89], ["larry", 898], ["marry", 98]]
# dict1 = dict(list3)#u can make any list a dictionray using this 
# print(dict1)
# for item in list1:#loops can call all the items at once
#     print(item)
# for item, burger, pest in list2:#u can use loops to call item and other function if there is a list in list 
#     print(item,"eats", burger, "burgers","and", pest,"pizza's")
# for item, burger in dict1.items():#it will work on dictionary to but first u will use .item function 
#     print(item,"eats", burger, "burgers")
# for item in dict1:#for only item it will print only the item in dictionary with no error 
#     print(item)

# list = ["harry","marry","carry", "darry"]
# list.append(65)
# list6 = ["cat","nat","pot", "no"]
# # dict2 = dict(list)
# print(list)
# for i  in list:
#     print(i)
#     if i == "carry":
#         break

# for i in list:
#     for j in list6:
        # print(i,j)
#quiz: make a list and then print only the numbers that exceeds 6 or greater than 6 
# #my solution:
# list4 =  [["harry",3], ["carry", 34], ["larry", 24], ["marry", 5]]
# for item, pest in list4:
#     if pest>6:#we can use if function within the for function for various uses 
#         print(pest)

# list = [23 , 34, 545, 534, 34,5455,"harry", 'carry']

# for i in list:
#     if str(i).isnumeric() and i>=35:
        # print(i)
#class solution 
"""list5 = ["harry", "carry", "larry", "marry", 6, 54, 87, 98, 34, 5, 2, 3, 4]
for item in list5:
    if str(item).isnumeric() and item>6:# .isnumeric function find the value of numeric words and if u want result then first convert the item to str().
        print(item)"""

# 17 tut class while loops:
"""i = 1
while (i<45): #while loops are use to do the same but it will keep running until the function is true 
    print(i) #if we print this it will repeat until data is true so thats why we will write a solution to end this below
    i = i + 1"""#we made here a condition so that it can stop after 45 because we used i<45 so it can end process

# break and continue statement #18
# i = 0 #true function in loop will execute the program over and over and dont stop until u stop it
# while (True):
#     if i+1<95:
#         i = i + 1
#         print(i)
#         continue
    
          
#     print(i + 1, end=" ")
#     if (i==100):
#          break #this function is use to stop the loop from running 
#     i = i + 1
# i = 0 
# while(i<50):
#     print(i)
#     i = i + 1 
# #quiz:

# while (True):
# p1 = int(input("enter your number\n "))
# if p1 <= 100:
#     continue
# else:
#     print("congrats your number exceed 100\n")
#     break


# T: task; 
# mal =['MALIK ABDULLAH', "TABISH", "ali", "anus", "fahad", "fariz"]
# for item in mal:
#     print(item.lower(), end=" ")
# # a=mal.lower()
# print(a)

# list1 = []
# while (True):
#     p1 = int(input("enter your number (enter 00 for exit) "))
#     if p1 == 00:
#         break
#     list1.append(p1)  
# print(list1)
# # # count = (list1)

# list1/ = []
# while(True):
#     d1 = int(input("enter your number for exit and displaying your list enter 00 "))
#     if d1 == 00 :
#         break
#     list.append(d1)
# print(list)

# list1 = [2,3,4,2,3,5,6,1,7]
# print(list1.count(24))
# print(len(list1))
# for i in range(len(list1)):
#     for j in range(i,len(list1)):
#         if list1[i]==list1[j]:
#             print(f"{list1[i]} is counted {list1[j]}")
2









    






    
         
  
 



































