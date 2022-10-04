##ss
import math
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        dicts = {}
        for x in range(len(nums)-1):
            for y in range(x+1,len(nums)):
                
                if nums[x]*nums[y] in dicts:
                    dicts[nums[x]*nums[y]]+=1
                    
                else:
                    dicts[nums[x]*nums[y]] = 1
                
        ans  = 0
        print(dicts)
        ##for every 2 pairs we will have 8 combinations
        ##if we have 6 pairs whose product is same
        ##ans would be 6C2 * 8
        ## 6C2 to choose any two pairs out of 6
        ##multiplied by 8 because each tuple of 4 numbers have 8 combinations
        for x in dicts:
            if dicts[x] >=2:
                ans+=math.comb(dicts[x],2)*8
                
        return ans
        
