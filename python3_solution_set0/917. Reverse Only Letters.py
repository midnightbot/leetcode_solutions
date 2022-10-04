##ss
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        
        temp = []
        
        fulls = [s[x] for x in range(len(s))]
        
        for x in range(len(fulls)):
            if (ord(fulls[x])>=97 and ord(fulls[x])<=122) or (ord(fulls[x])>=65 and ord(fulls[x])<=90):
                temp.append(fulls[x])
                fulls[x] = -1
                
        temp = temp[::-1]
        i = 0
        for x in range(len(fulls)):
            if fulls[x] == -1:
                fulls[x] = temp[i]
                i+=1
                
        ans = ""
        for x in range(len(fulls)):
            ans+=str(fulls[x])
            
        return ans
        
