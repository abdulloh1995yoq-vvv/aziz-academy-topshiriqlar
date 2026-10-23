n = int(input())
d = {}
for _ in range(n):
    kalit, qiymat = input().split()
    d[kalit] = int(qiymat)
natija = {k: f"{k}:{qiymat}" for k, qiymat in d.items()}
print(natija)