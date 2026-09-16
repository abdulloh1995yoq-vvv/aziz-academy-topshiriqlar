import sys

lines = sys.stdin.read().split()

if len(lines) >= 2:
    a = int(lines[0])
    b = int(lines[1])
    
    if a < b:
        print("Low")
        print("Correct")
    elif a > b:
        print("High")
        print("Correct")
    else:
        print("Correct")
elif len(lines) == 1:
    print("Correct")