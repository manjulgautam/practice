# print("hello world")
from traceback import print_tb

print("enter a number")
number=int (input())

for x in range(1,number+1):
    print(x,end=" ")

    if x%3==0 and x%5==0:
        print("c")
    elif x%3==0:
        print("a")
    elif x%5==0:
        print("b")
    else:
        print()




