def repeat(s, n=2):
    return s * n
s = input()
n = input()
print(repeat(s, int(n)) if n else repeat(s))