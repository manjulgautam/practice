# print("hello world")
from traceback import print_tb

print("enter a number")
number=int (input())

for x in range(1,number+1):
    print(x)

    if x%2==0:
        print("a")
    if x%3==0:
        print("b")
    if x%2==0 and x%3==0:
        print("c")
