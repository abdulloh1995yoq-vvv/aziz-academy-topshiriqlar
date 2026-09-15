topdi = False
for _  in range(3):
    if int(input()) == 8:
        print("Correct")
        topdi = True
        break
        
if not topdi:
    print("Game Over")