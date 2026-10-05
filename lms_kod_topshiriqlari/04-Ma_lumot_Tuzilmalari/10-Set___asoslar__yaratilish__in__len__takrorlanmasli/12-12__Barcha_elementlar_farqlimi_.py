a = list(map(int, input().split()))

if len(a) == len(set(a)):
    print("Ha")
else:
    print("Yo'q")