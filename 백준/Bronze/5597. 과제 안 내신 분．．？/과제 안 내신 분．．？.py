check =[i for i in range(1,31)]
for n in range(28):
    student = int(input())
    check.remove(student)

print(min(check))
print(max(check))