case = int(input())

for i in range(case) :
    student = list(map(int,input().split()))
    average = (sum(student)- student[0]) / student[0]
    count = 0
    for i in range(student[0]) :
        if student[i+1] > average  :
            count += 1
        else : 
            pass 
        per = count / student[0]*100 
    print(f'{per:.3f}%')