A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(map(int, input().split()))
only_A = A - B - C
only_B = B - A - C
only_C = C - A - B
result_set = only_A | only_B | only_C
if result_set:
    print(*sorted(result_set))
else:
    print("BO'SH")