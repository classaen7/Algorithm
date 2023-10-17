n = int(input())

five = n//5
three = 0

while five >= 0:
    if (n - five*5)%3 == 0:
        print(five+(n-5*five)//3)
        break
    else:
        five -= 1
else:
    print(-1)