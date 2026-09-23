n = int(input())
lst = list(map(int, input().split()))

copied_lst = list(lst)
copied_lst.reverse()

print(lst)
print(copied_lst)