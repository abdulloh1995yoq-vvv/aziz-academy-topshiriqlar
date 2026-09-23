n = int(input())
lst = list(map(int, input().split()))

musbatlar = [x for x in lst if x > 0]
print(musbatlar)