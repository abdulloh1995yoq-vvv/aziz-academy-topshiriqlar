n = int(input())

for i in range(1, 2 * n):
    k = i if i <= n else 2 * n - i
    print(" " * (n - k) + "*" * (2 * k - 1))