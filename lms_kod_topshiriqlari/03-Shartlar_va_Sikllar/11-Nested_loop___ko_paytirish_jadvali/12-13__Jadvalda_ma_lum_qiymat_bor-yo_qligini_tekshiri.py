n, m = map(int, input().split())
x = int(input())

s = set()

for i in range(1, n + 1):
    for j in range(1, m + 1):
        s.add(i*j)
        
print("Yes" if x in s else "No")