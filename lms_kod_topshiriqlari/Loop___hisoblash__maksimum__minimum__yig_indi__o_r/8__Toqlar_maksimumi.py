n = int(input())
a = list(map(int, input().split()))

mx = None

for i in a:
    if i % 2 != 0:
        if mx is None or i > mx:
            mx = i
            
if mx is None:
    print("No")
else:
    print(mx)