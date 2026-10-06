n = int(input())
total_score = 0
for _ in range(n):
    name, score = input().split()
    total_score += int(score)
    
print(total_score / n)