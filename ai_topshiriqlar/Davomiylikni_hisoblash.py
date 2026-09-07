# Davomiylikni hisoblash
# Kurs: Dasturlash / IT
# Mavzu: Sonlar: int va float — butun va kasr sonlar
# Ball: 100
# Aziz Academy — AI Topshiriq

h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

boshlanish = h1 * 60 + m1 
tugash = h2 * 60 + m2 

farq = tugash - boshlanish 

soat = farq // 60
daqiqalar = farq % 60

print(soat)
print(daqiqalar)