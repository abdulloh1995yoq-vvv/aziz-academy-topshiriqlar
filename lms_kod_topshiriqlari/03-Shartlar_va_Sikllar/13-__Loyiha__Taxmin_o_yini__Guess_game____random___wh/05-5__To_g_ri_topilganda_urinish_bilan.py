tries = 0
while True:
    guess = int(input())
    tries += 1
    if guess == 4:
        print(f"Correct in {tries} tries")
        break