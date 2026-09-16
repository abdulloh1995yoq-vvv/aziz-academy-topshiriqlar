import sys

deta = sys.stdin.read().split()
count = 0
i = 0

while i < len(deta):
    if int(deta[i]) == 0:
        break
    count += 1
    i += 3
print(count)