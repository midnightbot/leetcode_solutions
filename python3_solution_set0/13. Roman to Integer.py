##ss
class Solution:
    def romanToInt(self, s: str) -> int:
        
        dicts = {}
        dicts["I"] = 1
        dicts["V"] = 5
        dicts["X"] = 10
        dicts["L"] = 50
        dicts["C"] = 100
        dicts["D"] = 500
        dicts["M"] = 1000
        
        i = 0
        ans = 0
        while i < len(s):
            if i+1 < len(s):
                if dicts[s[i+1]] > dicts[s[i]]:
                    ans+=dicts[s[i+1]] - dicts[s[i]]
                    i+=2
                    
                else:
                    ans+=dicts[s[i]]
                    i+=1
                    
            else:
                ans+=dicts[s[i]]
                i+=1
                
        return ans
                    
        
