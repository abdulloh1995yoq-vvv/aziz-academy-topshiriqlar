import sys

data = sys.stdin.read().split()
if data:
    n = int(data[0])
    nums = list(map(int, data[1:]))
    first, *mid, last = nums
    print(first)
    print(mid)
    print(last)