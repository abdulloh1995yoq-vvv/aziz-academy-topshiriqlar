n = int(input())
a = list(map(int, input().split()))

x = a[0]

for i in a:
    if a.count(i) > a.count(x) or (a.count(i) == a.count(x) and i < x):
        x = i
        
print(x)
