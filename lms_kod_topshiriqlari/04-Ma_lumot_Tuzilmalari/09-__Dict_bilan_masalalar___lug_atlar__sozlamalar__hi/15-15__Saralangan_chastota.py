s = input().strip()
for c in sorted(set(s)):
    print(f"{c}={s.count(c)}")