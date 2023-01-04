word = input().lower()
word_set = list(set(word))
com = []
for i in word_set :
    count = word.count(i)
    com.append(count)       

if com.count(max(com)) >= 2 :
    print('?')
else:
    print(word_set[(com.index(max(com)))].upper())