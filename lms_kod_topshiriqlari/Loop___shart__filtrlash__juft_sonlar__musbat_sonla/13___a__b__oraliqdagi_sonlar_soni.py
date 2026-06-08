n = int(input())
a1 = list(map(int, input().split()))
a, b = map(int, input().split())

print(sum(1 for x in a1 if a <= x <= b))