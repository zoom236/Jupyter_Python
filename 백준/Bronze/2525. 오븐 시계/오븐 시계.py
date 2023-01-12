H,M = map(int,input().split())
cook = int(input())
M2 = cook + M    
if M2 >= 60 :
    H += (M2 // 60) 
    M = (M2) % 60
    if H >= 24 :
        H -= 24
else :
    M = M2     

print(H,M)