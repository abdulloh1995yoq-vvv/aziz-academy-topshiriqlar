n = int(input())
sonlar = list(map(int, input().split()))
res = []
for x in sonlar:
    res.insert(0, x)
    
print(res)