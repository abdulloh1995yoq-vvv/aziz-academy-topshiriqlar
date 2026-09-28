n = int(input())
min_qiymat = -1
min_kalit = ""

for _ in range(n):
    kalit, qiymat = input().split()
    
    if min_qiymat == -1 or qiymat < min_qiymat:
        min_qiymat = qiymat
        min_kalit = kalit
        
print(min_kalit)