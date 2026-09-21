import sys

l = []
for line in sys.stdin:
    c = line.split()
    if c[0] == 'stop':print(l);break
    try:getattr(l, c[0])(*(int(x) for x in c[1:]))
    except:0