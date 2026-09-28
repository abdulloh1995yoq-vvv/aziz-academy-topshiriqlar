import sys

L = sys.stdin.read().split()[1:]
print(max(L, key=L.count))