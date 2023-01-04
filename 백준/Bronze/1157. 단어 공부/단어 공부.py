word = input().lower() #소문자로 변경
word_set = list(set(word)) #set 집합함수를 통해, 중복제거 
com = []
for i in word_set :
    count = word.count(i) #처음 입력된 단어에서 중복 된 알파벳 갯수 세기 
    com.append(count)       

if com.count(max(com)) >= 2 : #max가 같은 수로 2개 이상일때 
    print('?')
else:
    print(word_set[(com.index(max(com)))].upper())
    #ex) word = baaa
    #ex) word_set = [b,a]
    #ex) com = [1,3]
    #max(com)은 3 index(3)은 com[1]에 위치 word_set[1]은 a를 가리킴