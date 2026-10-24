def clamp(x, lo, hi):
    return max(lo, min(x, hi))
x, lo, hi = map(int, input().split())
print(clamp(x, lo, hi))
print(clamp(lo=lo, hi=hi, x=x))