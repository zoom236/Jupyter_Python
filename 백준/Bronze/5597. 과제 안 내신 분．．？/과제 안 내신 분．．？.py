idx = [number for number in range(1,31)]
for i in range(28) :
    students = int(input())
    idx.remove(students)

print(min(idx),max(idx), sep='\n' )

    