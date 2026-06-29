# Valyuta almashish dasturi
# Kurs: Dasturlash / IT
# Mavzu: Sonlar: int va float — butun va kasr sonlar
# Ball: 100
# Aziz Academy — AI Topshiriq

miqdor = float(input())
qolgan = input().strip().lower()

kurs = 0.8872

if qolgan == "dollar":
    t = input().strip().lower()
    if t == "eyvro":
        natija = miqdor * kurs
        print("%.2f" % natija)
        
elif qolgan == "eyvrodollar":
    natija = miqdor / kurs 
    print("%.2f" % natija)