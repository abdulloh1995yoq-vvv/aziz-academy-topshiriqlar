s = input()
print(" ".join(f"{c}:{s.count(c)}" for c in dict.fromkeys(s)))