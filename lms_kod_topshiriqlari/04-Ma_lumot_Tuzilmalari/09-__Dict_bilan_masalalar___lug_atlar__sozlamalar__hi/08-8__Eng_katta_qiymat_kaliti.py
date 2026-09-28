n = int(input())
max_qiymat = -1
max_kalit = ""

for _ in range(n):
    kalit, qiymat = input().split()
    qiymat = int(qiymat)
    
    if max_qiymat == -1 or qiymat > max_qiymat:
            max_qiymat = qiymat
            max_kalit = kalit
print(max_kalit)