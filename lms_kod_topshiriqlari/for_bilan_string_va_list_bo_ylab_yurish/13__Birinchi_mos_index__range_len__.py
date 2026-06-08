n = int(input())
a = list(map(int, input().split()))
x = int(input())
i = 0 
while i < n:
    if a[i] == x:
        print(i)
        break
    i += 1
else:
    print(-1)