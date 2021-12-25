##ss
class Solution:
    def countLetters(self, s: str) -> int:
        
        ans = 0
        
        for x in range(len(s)):
            temp = ""
            temp+=s[x]
            ans+=1
            #ans.append(temp)
            for y in range(x+1,len(s)):
                if s[y] == temp[len(temp)-1]:
                    temp+=s[y]
                    ans+=1
                    #ans.append(temp)
                    
                else:
                    break
                    
        return ans
                
        
