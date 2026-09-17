import sys

s = sys.stdin.read().split()
if s[0].isdigit():
    n = int(s[0])
    print(s[1], [int(x) for x in s[2:n]], s[n], sep='\n')
else:
    for t in s:
        if t == 'stop':
            break
        print('Working')