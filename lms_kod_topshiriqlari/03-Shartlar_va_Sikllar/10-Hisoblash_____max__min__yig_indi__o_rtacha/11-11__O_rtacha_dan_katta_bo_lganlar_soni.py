n = int(input())
a = list(map(int, input().split()))

s = sum(a) / n
print(len([x for x  in a if x > s]))