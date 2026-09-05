# Kirish nazorati
# Kurs: Dasturlash / IT
# Mavzu: Bool va mantiq — True/False, mantiqiy ifodalar
# Ball: 100
# Aziz Academy — AI Topshiriq

yosh = int(input())
boy = int(input())

yosh_mos = yosh >= 14
boy_mos = boy >= 120

if yosh_mos and boy_mos:
    print("ruxsat")
elif yosh_mos or boy_mos:
    print("kuzatuvchi bilan")
else:
    print("ruxsat emas")