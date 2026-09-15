secret = 42

while True:
    g = int(input())
    if g > secret:
        print("High")
    elif g < secret:
        print("Low")
    else:
        print("Correct")
        break