H,M = map(int,input().split(' '))
    
if M < 45 :
    M = 60 + (M - 45)
    if H == 0 :
        H = 23
    else : 
        H -= 1
else :
    M = M - 45     

print(H,M)