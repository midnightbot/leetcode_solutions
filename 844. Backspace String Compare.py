class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        return self.construct(s) == self.construct(t)
        
    def construct(self,strs):
        ans = []
        
        for x in range(len(strs)):
            if strs[x]!="#":
                ans.append(strs[x])
                
            else:
                if len(ans)!=0:
                    ans.pop()
                
                
        return "".join(ans)
        
