n = int(input())

if n <= 1:
    print(0)
else:
    ans = 0 
    for i in range(2, n + 1):
        if n % i ==0:
            ans = i 
            break
    print(ans)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    