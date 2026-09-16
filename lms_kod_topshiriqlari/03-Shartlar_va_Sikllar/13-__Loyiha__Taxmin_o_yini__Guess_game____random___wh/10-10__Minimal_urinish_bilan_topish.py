import sys

count = 0
for x in sys.stdin.read().split():
    v = int(x)
    count += 1
    if v == 1:
        print("Correct")
        print(count)
        break
    else:
        print("Try again")