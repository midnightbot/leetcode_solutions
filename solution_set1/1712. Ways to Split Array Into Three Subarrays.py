class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        
        ## sum(left) <= sum(mid) <= sum(right)
        
        mods = 10**9 + 7
        
        pre = [0]
        
        for x in nums:
            pre.append(pre[-1] + x)
            
        total = pre[-1]  
        ans = 0
        for x in range(1,len(nums)-1):
            if pre[x] > total / 3:
                break
                
            i = bisect_left(pre,pre[x]*2,x+1,len(nums))
            j = bisect_left(pre,(total+pre[x])//2 + 1,i,len(nums))
            
            ans+= (j-i)
            ans%=mods
            
        return ans%mods
            
