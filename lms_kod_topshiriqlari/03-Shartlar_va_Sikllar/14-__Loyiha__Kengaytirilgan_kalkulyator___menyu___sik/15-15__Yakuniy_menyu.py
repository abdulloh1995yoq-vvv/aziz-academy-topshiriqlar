a, b = map(int, input().split())
while (c := int(input())):
    print([a+b, a-b, a*b, a/b][c-1])
print("Exit")