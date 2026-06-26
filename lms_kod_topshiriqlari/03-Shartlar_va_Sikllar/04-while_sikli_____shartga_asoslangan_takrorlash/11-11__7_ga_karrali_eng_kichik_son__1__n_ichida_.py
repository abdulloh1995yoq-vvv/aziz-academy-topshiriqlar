n = int(input())
x = 1

while x <= n:
    if x % 7 == 0:
        print(x)
        break
    x += 1
else:
        print("No")