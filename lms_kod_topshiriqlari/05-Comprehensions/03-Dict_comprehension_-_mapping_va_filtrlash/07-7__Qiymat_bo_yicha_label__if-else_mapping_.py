n = int(input())
print({(l := input().split())[0]: ('even' if int (l[1]) % 2 == 0 else 'odd')for _ in range(n)})