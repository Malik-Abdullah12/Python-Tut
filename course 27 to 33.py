#tut 27 : exercize solution in video 
#tut 28: Writing And Appending To A File :


# f = open("openfile.txt", "w")#w is the code of write
# f = open("openfile.txt2", "a")#a is the code of appending a file 
# # f.write("this file is the example of writing a new file from within  a code\n")#\n for new line 
# a = f.write("this file is the example of writing a new file from within  a code\n")#\n for new line 
# print(a)#this code is used to know the numebr of characters u wrote in the data 
# f.close()

# f= open("openfile.txtw3", "r+")
# print(f.read())
# f.write("thank you well it is ")
# f.close()
# exit

#code from website
# print("How Many Row You Want To Print")
# p1= int(input())
# print("Type 1 Or 0")
# p2 = int(input())
# new =bool(p2)
# if new == True:
#     for i in range(1,p1+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif new ==False:
#     for i in range(p1,0,-1):
#         for j in range(1,i+1):
#             print("*", end="")
#         print()

#code from website.
# print("Draw a star pattern for right angle triangle")
# p1 = int(input("Enter number of rows: "))
# print("Enter boolean operator 0 or 1")
# a = int(input())
# b = bool(a)
# if b==1:
#     for i in range(1,p1+1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()
# elif b==0:
#     for i in range(p1,0,-1):
#         for j in range(1,i+1):
#             print("*",end=" ")
#         print()

#29 : exercize 4 karni hai :

# #30 :Seek(), tell() & More On Python Files
# f = open("tes.py")
# print(f.tell())#tell function tells the value of your line in numbers for ex "harry" is of 4 char;
# print(f.readline())#readline reads a line from your file you are showing and displaying in it 
# print(f.tell())
# f.seek(2)#seek() function is used to change the position of the File Handle to a given specific position
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
# f.close()


#31 : Using With Block To Open Python Files:
# with open("openfile.txt") as f :
#     b = f.read(90)
#     print(b)
# # ANs: yes it will work if you give a new command of opening a file outside the with block function 
# f= open("openfile.txt2")
# print(f.read())

# f.close()

#32 exercize health managment system


#33 Scope, Global Variables and Global Keyword;

# l = 10 # Global

# def function1(n):
#     # l = 5 #Local
#     m = 8 #Local
#     global l # global keywords 
#     l = l + 45
#     print(l, m)
#     print(n, "I have printed")

# function1("This is me")
# # print(m)

# x = 89
# def harry():
#     x = 20
#     def rohan():
#         global x
#         x = 88
#     # print("before calling rohan()", x)
#     rohan()
#     print("after calling rohan()", x)

# harry()
# print(x)



  









# # x = range(54,98,9)
# for n in x:
#     print(n)#The range() function returns a sequence of
#  numbers, starting from 0 by default, and increments by 1 
# (by default), and stops before a specified number.

# def function6(i):
#     sum1 = int(input('enter your number\n'))
#     # i = 1
#     # i = i + 1 
#     i = 1
#     sum = i + sum1/2
#     print(sum)
# function6(1) 

# def function8():
#     n = int(input("enter your number u like to sum "))
#     sum=0
#     for item in range(n+1):
#         sum= sum+item    
#     print("Sum: ",sum)
        
# function8()
# # sum = a + sum1
# #         print(sum)
   