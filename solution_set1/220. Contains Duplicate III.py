class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        ## abs(nums[i] - nums[j]) <=t and abs(i-j) <=k
        
        ## we can use buckets,  add numbers into buckets of thousands, but still worst case can be n**2
        ##basically this is a type of improved sliding window 
        check = OrderedDict()

        for number in nums:
            
            if len(check) > k:
                check.popitem(last=False) ##removing the first added element
                
            b = number // (t or 1)
            
            for z in range(b-1,b+2):
                if z in check and abs(number - check[z])<=t:
                    return True
                
            check[b] = number
            
        return False
            
        
