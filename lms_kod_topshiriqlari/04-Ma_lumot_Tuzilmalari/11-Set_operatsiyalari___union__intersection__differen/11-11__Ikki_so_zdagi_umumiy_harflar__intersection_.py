a = set(input().strip())
b = set(input().strip())
common = sorted(a & b)
if common:
    print("".join(common))
else:
    print("BO'SH")