##ss
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        ##flip at most one zero
        ## find all 1 groups
        ## see which 2 groups(max) is connected by a zero
        comp = []
        count = 0 
        for x in range(len(nums)):
            if nums[x] == 1:
                count+=1
                
            else:
                comp.append(count)
                comp.append(0)
                count = 0
                
        if count!=0:
            comp.append(count)
            
        ans = 0
        
        for x in range(len(comp)):
            if comp[x]!=0:
                ans = max(ans,comp[x])
                
            else:
                if x == 0:
                    ans = max(ans, comp[x+1] + 1)
                    
                elif x == len(comp)-1:
                    ans = max(ans, comp[x-1] + 1)
                    
                else:
                    ans = max(ans, comp[x-1] + 1 + comp[x+1])
                    
                    
        return ans
