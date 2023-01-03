n = int(input())
han = 0 
for i in range(1,n+1) :
    if i < 100 :
        han += 1
    else :
        n_str = list(map(int,str(i)))
        if n_str[2]-n_str[1] == n_str[1] - n_str[0]:
            han +=1
            
print(han)