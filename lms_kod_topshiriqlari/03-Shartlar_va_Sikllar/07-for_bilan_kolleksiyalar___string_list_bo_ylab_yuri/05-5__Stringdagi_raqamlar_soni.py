s = input()

n = 0
for i in s:
    if i in "0123456789":
        n += 1
        
print(n)