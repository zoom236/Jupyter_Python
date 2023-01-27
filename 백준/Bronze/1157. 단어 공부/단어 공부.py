word = input().lower()
word_set = list(set(word))
temp= []
for i in word_set :
    count = word.count(i)
    temp.append(count)
if temp.count(max(temp)) >= 2 :
    print("?")
else :
    print(word_set[(temp.index(max(temp)))].upper())
