n = int(input())
d = {}
for _ in range(n):
    k, v = input().split()
    d[int(k)] = int(v)
for key, value in d.items():
    print(key + value)