n = int(input())

for i in range(n):
    s = ''
    for j in range(n):
        if i == j or i + j == n-1:
            s += "*"
        else:
            s+='.'
    print(s)