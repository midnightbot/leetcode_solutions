import itertools
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        
        mods = 10**9 + 7
        
        temp = {}
        
        for x in nums:
            temp[x-int(str(x)[::-1])] = temp.get(x-int(str(x)[::-1]),0) + 1
            
        ans = 0
        
        for x in temp:
            ans+=comb(temp[x],2)
            ans%=mods
        return ans%mods
