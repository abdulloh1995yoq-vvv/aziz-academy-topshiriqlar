n = int(input())
lst = list(map(int, input().split()))

toqlar = [x for x in lst if x % 2 != 0]
print(toqlar)