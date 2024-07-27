import sys
import math
# A, B, C = map(int, sys.stdin.readline().split())

def solve():
    def num_to_char(n):
        re = ""
        if n % 3 == 0:
            re += "Fizz"
        if n % 5 == 0:
            re += "Buzz"
        if re == "":
            re = str(n)
        
        return re
    
    lst = []
    for i in range(3):
        lst.append(input())
    
    for i in range(3):
        num = lst[i]
    
        if num == 'Fizz' or num == 'Buzz' or num == 'FizzBuzz':
            continue
        else:
            return num_to_char(int(num) + (3-i))

print(solve())

"""
1
2
F
4
B
F


"""
