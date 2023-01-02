n = int(input())

for i in range(n) :
    test = list(input())
    score = 0
    oo = 0
    for case in test :
        if case == 'O' :
            oo += 1
            score += oo
        else : 
            oo = 0 
    print(score)
