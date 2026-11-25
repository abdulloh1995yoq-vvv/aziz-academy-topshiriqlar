c = 0
for _ in range(int(input())):
    c = c + 1 if input().strip() == "inc" else 0
    print(c)