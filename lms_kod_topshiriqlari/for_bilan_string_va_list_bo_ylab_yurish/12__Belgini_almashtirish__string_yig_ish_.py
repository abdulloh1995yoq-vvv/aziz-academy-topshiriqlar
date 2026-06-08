s = input()

t = ""

for i in s:
    if i == 'a':
        t += '@'
    else:
        t += i
        
print(t)