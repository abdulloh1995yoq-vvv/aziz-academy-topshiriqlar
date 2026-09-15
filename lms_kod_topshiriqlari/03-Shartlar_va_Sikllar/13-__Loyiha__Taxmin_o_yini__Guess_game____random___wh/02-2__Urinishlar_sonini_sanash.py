secret = 5
attempts = 0

while True:
    g = int(input())
    attempts += 1
    if g == secret:
        print(attempts)
        break