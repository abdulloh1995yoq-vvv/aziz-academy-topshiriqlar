import sys

words = sys.stdin.read().split()
n = int(words[0])
lst = words[1 : n + 1]
target = words[n + 1]

d = {}
for w in lst:
    d[w] = d.get(w, 0) + 1
    
print(d.get(target, 0))