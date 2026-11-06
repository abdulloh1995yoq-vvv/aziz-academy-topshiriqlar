def join3(a, b='-', c='-'):
    return f"{a} {b} {c}"
s = (input().split() + ['-', '-'])[:3]
print(join3(*s))