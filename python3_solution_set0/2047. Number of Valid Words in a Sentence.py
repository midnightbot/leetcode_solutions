class Solution:
    def countValidWords(self, sentence: str) -> int:
        
        temp = sentence.split()
        #print(temp)
        #print(temp)
        #print(sentence)
        ans = []
        token = 0
        #print(temp)
        for x in range(len(temp)):
            hyphen = 0
            punc = 0
            invalid = 0
            for y in range(len(temp[x])):
                #print(temp[x][y])
                if temp[x][y] == '-':
                    hyphen+=1
                    if y == 0 or y == len(temp[x])-1:
                        invalid = 1
                        
                    elif ord(temp[x][y-1])<97 or ord(temp[x][y-1])>122:
                        invalid = 1
                        
                    elif ord(temp[x][y+1])<97 or ord(temp[x][y+1]) > 122:
                        invalid = 1
                    
                elif temp[x][y] == '.' or temp[x][y] == ',' or temp[x][y] == '!':
                    punc+=1
     
                elif ord(temp[x][y]) >=48 and ord(temp[x][y])<=57:
                    invalid = 1
                    break
                    
            if hyphen>=2 or punc>=2:
                invalid = 1
                
            
            if hyphen<=1 and punc<=1 and invalid==0:
                if hyphen == 1 and invalid ==0 :
                    if temp[x][0] == '-' or temp[x][len(temp[x])-1] == '-':
                        invalid = 1
                        
                    else:
                        invalid = 0
                        
                
                if punc == 1 and invalid==0:
                    if temp[x][len(temp[x]) - 1] == '.' or temp[x][len(temp[x]) - 1] == ',' or temp[x][len(temp[x]) - 1] == '!':
                        invalid = 0
                        
                    else:
                        invalid = 1
                        
                        
            if invalid == 0:
                token+=1
                ans.append(temp[x])
        print(ans)        
        return token
                    
            
        
