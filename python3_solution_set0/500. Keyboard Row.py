##ss
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        row1 = ['q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P']
        row2 = ['a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L']
        row3 = ['z','x','c','v','b','n','m','Z','X','C','V','B','N','M']
        ans  = []
        for x in range(len(words)):
            a=0
            b=0
            c=0
            for y in range(len(words[x])):
                if words[x][y] in row1:
                    a+=1
                elif words[x][y] in row2:
                    b+=1
                    
                else:
                    c+=1
                    
            if a==0 and b==0:
                ans.append(words[x])
                
            elif a==0 and c==0:
                ans.append(words[x])
                
            elif b==0 and c==0:
                ans.append(words[x])
                    
        return ans
