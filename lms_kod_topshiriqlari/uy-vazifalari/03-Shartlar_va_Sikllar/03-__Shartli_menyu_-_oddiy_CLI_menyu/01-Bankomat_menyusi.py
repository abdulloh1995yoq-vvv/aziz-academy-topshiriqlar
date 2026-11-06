o, b, s = int(input()), int(input()), int(input())
print(b if o == 1 else b - s if o == 2 and b>= s else "Mablag' yetarli emas" if o == 2 else b + s if o == 3 else "Notogri amal")