n = int(input())
scores = [int(input().split()[1]) for _ in range(n)]
print(max(scores))