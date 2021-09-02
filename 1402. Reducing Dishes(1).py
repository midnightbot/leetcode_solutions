class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        ans = 0
        maxs = 0
        satisfaction = sorted(satisfaction)
        print(satisfaction)
        
        for x in range(len(satisfaction)):
            ans += satisfaction[x] * (x+1)
            
        if max(satisfaction) < 0:
            return 0
        
        else:
            temp = sum(satisfaction)
            while temp <= 0:
                
                ans = ans - temp
                #print(ans)
                satisfaction.pop(0)
                temp = sum(satisfaction)
            return ans
                
                
            
        
        
        
