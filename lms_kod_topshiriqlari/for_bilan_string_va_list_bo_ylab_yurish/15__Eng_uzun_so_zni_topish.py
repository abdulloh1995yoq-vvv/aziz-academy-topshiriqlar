s = input().split()

eng = ""
for i in s:
    if len(i) > len(eng):
        eng = i
print(eng)