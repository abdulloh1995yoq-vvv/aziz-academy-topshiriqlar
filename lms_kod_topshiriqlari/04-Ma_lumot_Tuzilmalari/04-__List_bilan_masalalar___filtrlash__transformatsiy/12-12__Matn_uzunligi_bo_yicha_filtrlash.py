n = int(input())
words = input().split()
result = [w for w in words if len(w) >= n]
print(result)