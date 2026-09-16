import sys

c = 0
for x in sys.stdin.read().split():
    v = int(x)
    c += 1
    print("Invalid" if not 1 <= v <= 20 else "Low" if v < 20 else "High" if  v > 20 else "Correct")
    if v == 20:
        print(c)
        break