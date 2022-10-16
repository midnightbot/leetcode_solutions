class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        seen = set(nums)
        
        for x in nums:
            seen.add(int(str(x)[::-1]))
            
        return len(seen)
        
