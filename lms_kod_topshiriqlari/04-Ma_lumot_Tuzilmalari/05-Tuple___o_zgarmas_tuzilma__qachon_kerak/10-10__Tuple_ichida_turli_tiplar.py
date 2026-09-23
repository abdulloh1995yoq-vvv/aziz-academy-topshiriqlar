x = input().split()
res = [
    int(i) if i.isdigit() else float(i) if "." in i else i for i in x
]

print(tuple(res))