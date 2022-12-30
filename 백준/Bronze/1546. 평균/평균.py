test = int(input())
score = list(map(int,input().split()))
max_score = max(score)

for i in range(test) :
    score[i] = score[i] / max_score * 100 
    
s = sum(score)
    
print(s/test)
