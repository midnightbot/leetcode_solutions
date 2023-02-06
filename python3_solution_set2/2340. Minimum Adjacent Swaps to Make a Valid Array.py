class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:

        lindx = nums.index(min(nums))

        ans = 0
        rindx = nums[::-1].index(max(nums))
        
        if len(nums) - rindx <= lindx:
            return max(rindx + lindx - 1,0)
        else:
            return max(rindx + lindx , 0)
