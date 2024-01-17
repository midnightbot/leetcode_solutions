class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                ans = nums[x] | nums[y]
                ans = format(ans, 'b')
                ans = str(ans)
                if ans[-1] == '0':
                    print(nums[x], nums[y], ans)
                    return True
                
        return False
        
