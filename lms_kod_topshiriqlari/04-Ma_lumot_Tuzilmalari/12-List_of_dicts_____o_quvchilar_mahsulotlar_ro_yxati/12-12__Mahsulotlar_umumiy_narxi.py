n = int(input())
total_price = 0
for _ in range(n):
    name, price = input().split()
    total_price += int(price)
    
print(total_price)