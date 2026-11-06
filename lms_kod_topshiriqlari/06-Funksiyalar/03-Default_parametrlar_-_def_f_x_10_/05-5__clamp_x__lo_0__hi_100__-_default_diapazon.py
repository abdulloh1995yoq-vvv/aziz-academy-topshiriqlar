def clamp(x, lo=0, hi=100):
    return max(lo, min(int(x), hi))
print(clamp(*map(int, input().split())))