##ss
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        ans = 0
        mins = float('inf')
        for x in range(len(strs)):
            mins = min(mins,len(strs[x]))
        if len(strs) == 0 :
            return ""
        
        elif len(strs) == 1:
            return strs[0]
        
        for x in range(mins):
            if ans < mins:
                for y in range(1,len(strs)):
                    if strs[y][ans] != strs[y-1][ans]:
                        break

                if strs[y][ans] == strs[y-1][ans]:
                    ans+=1
                
        if ans == 0:
            return ""
        
        else:
            #return ans
            return strs[0][0:ans]
        
