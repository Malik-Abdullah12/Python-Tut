print("Astrologers Stars: ")
p1= int(input("how many stars row u want ?"))
print("enter boolean operator 1 or 0 , to start operation")
a = int(input())
b = bool(a)

if b==1:
    for i in range(1,p1+1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()
elif b == 0:
    for i in range(p1,0,-1):
        for j in range(1,i+1):
            print("*", end=" ")
        print()




