def calc(x, y):
    return x + y, x * y

a, b = map(int, input().split())
s, p = calc(a, b)
print(s)
print(p)