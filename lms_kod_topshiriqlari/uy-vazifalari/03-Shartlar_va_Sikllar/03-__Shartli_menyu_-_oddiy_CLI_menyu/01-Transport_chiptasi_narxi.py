t, k = int(input()), int(input())
print(
    'Notogri transport' if t not in (1, 2, 3) else
    'Notogri toifa' if k not in (1, 2, 3) else
    (4000 if t == 3 else 1700) // (2 if k == 2 else 1) if k != 3 else 0
)