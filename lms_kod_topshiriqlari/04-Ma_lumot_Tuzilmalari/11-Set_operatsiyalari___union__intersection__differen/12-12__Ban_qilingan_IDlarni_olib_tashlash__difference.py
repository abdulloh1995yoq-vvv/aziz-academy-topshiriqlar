ids = set(map(int, input().split()))
banned = set(map(int, input().split()))
_ = input()  
allowed = sorted(ids - banned)
if allowed:
    print(*allowed)
else:
    print("BO'SH")