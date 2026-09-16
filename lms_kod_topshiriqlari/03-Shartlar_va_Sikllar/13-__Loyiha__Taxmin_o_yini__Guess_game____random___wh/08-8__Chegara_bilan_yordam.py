import sys

for x in sys.stdin.read().split():
    v = int(x)
    if v == 15:
        print("Correct")
        break
    print("Far" if abs(v - 15) >= 5 else "Close")