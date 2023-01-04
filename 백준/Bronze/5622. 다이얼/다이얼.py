dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
tele = list(input())
time = 0 
for i in range(len(tele)):
    for j in dial :
        if tele[i] in j :
            time += dial.index(j)+3 
print(time)