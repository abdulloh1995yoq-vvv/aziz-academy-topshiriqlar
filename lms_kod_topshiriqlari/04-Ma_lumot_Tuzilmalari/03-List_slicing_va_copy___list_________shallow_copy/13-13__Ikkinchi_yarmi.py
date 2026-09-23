n = int(input())
lst = list(map(int, input().split()))

mid = len(lst) - len(lst) // 2
print(lst[mid:])