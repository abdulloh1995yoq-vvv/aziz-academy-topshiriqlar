n = int(input())

m=n//2

for i in range(n):
    s = ''
    for j in range(n):
        if i==m or j==m:
            s += '*'
        else:
            s+='.'
    print(s)