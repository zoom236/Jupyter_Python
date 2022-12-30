num_list = []
for i in range(9):
    num = int(input())
    num_list.append(num)
    
print(max(num_list))
for i in range(9) :
    if max(num_list) == num_list[i] :
        print(i+1)
    else :
        pass
