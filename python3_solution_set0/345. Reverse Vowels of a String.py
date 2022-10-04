##ss
class Solution:
    def reverseVowels(self, s: str) -> str:
        
        ans = ""
        temp1 = []
        temp2 = []
        strs = []
        for x in range(len(s)):
            if s[x] == "a" or s[x] == "A" or s[x] == "e" or s[x] == "E" or s[x] == "i" or s[x] == "I" or s[x] =="o" or s[x] == "O" or s[x] == "u" or s[x] == "U":
                temp1.append(s[x])
                strs.append(1)
                
            else:
                temp2.append(s[x])
                strs.append(2)
                
        temp1 = temp1[::-1]
        
        c1 = 0
        c2 = 0
        
        for x in range(len(strs)):
            if strs[x] == 1:
                ans+=temp1[c1]
                c1+=1
                
            else:
                ans+=temp2[c2]
                c2+=1
                
        return ans
                
         
