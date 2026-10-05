A = set(input().strip().split())
B = set(input().strip().split())

common = sorted(list(A & B))
print(len(common))
for name in common:
    print(name)