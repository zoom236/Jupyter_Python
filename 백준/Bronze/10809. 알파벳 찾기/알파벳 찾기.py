s = input()
askii = list(range(97,123)) #알파벳 26자 97~122 

for alpha in askii : 
    print(s.find(chr(alpha)))