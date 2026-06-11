n = int(input())
a = list(map(int, input().split()))
k = int(input())

ans = a[0]
for x in a:
    d = abs(x - k)
    if d < abs (ans - k) or (d == abs(ans - k) and x < ans):
        ans = x
print(ans)