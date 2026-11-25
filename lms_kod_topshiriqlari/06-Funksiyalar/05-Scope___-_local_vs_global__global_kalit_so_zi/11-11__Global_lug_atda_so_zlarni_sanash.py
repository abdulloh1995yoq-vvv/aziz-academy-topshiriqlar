from collections import Counter
for k, v in sorted(Counter(input().strip().lower() for _ in range(int(input()))).items()):
    print(k,v)