import sys

for x in sys.stdin.read().split():
    v = int(x)
    if v == 0:
        print("Exit")
    elif v == 3:
        print("Correct")
    elif v < 3:
        print("Low")
    else:
        print("High")