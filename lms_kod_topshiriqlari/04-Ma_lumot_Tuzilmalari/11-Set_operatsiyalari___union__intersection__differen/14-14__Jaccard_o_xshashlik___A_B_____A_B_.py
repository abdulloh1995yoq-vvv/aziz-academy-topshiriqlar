A = set(map(int, input().split()))
B = set(map(int, input().split()))

intersection_size = len(A & B)
union_size = len(A | B)

jaccard = intersection_size / union_size
print(f"{jaccard:.3f}")