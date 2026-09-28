import sys 
data = sys.stdin.read().split()
d = {f"k{i}": int(x) for i, x in enumerate(data[1:])}
print(sum(d.values()))