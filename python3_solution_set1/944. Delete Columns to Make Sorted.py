##ss
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        ans = 0
        
        for x in range(len(strs[0])):
            temp = ""
            for y in range(len(strs)):
                temp+=strs[y][x]
            
            #print(temp,sorted(temp))
            if temp!=''.join(sorted(temp)):
                ans+=1
                
        return ans
                
        
