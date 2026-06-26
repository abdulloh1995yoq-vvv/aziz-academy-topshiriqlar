n = int(input())
a = list(map(int, input().split()))

mn = None

for i in a:
    if i % 2 == 0:
        if mn is None or i < mn:
            mn = i
            
if mn is None:
    print("No")
else:
    print(mn)