##ss
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        memo = {}
        
        prefix =  [0]
        sums = 0
        for x in range(len(nums)):
            sums+=nums[x]
            prefix.append(sums)
            
        #print(prefix)
        self.n = len(nums)
        return self.divide(prefix,0,m,nums,memo)
        
        
    def divide(self,prefix,indx,m,nums,memo):
        ans = prefix[self.n]
        if m == 1:
            return prefix[self.n] - prefix[indx]
        
        elif (indx,m) in memo:
            return memo[(indx,m)]
        
        
        else:
            for x in range(indx, self.n - m + 1):
                thissum = prefix[x+1] - prefix[indx]
                
                aftersplit = max(thissum, self.divide(prefix,x+1,m-1,nums,memo))
                
                ans = min(ans,aftersplit)
                
            
                if thissum >= ans:
                    break
                    
            memo[(indx,m)] = ans
            return memo[(indx,m)]
            
                
                
                
                
        
        
