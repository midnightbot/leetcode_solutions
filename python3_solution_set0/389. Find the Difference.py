class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = [str(x) for x in t]
        
        print(ans)
        for x in range(len(s)):
            ans.remove(s[x])
            
        #print(ans)
        return ans[0]
        
