s = c = 0

while (n := int(input())):
    s += n
    c += 1
print(0 if c == 0 else s / c)