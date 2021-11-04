class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        counter = 0
        ans = []
        if s == "":
            return True
        
        for x in range(len(t)):
            if len(ans) == len(s):
                return True
        
            if t[x] == s[counter]:
                ans.append(x)
                counter+=1
                
        if len(ans) == len(s):
            return True
        
        else:
            return False
        
