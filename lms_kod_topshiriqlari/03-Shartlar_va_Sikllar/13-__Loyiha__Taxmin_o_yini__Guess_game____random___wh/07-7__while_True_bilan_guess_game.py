import sys 

for x in sys.stdin.read().split():
    v = int(x)
    if v < 9:
        print("Low")
    elif v > 9:
        print("High")
    else:
        print("Correct")
        break