##ss
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        temp = ""
        temp+=s[0]
        for x in range(1,len(s)):
            if len(temp)%k!=0:
                temp+=s[x]
                
            else:
                ans.append(temp)
                temp = ""
                temp+=s[x]
                
        for y in range(k-len(temp)):
            temp+=fill
            
        ans.append(temp)
        return ans
        
