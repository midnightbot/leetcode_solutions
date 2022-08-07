class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        
        n = len(nums)
        count = 0
        for x in range(n-2):
            for y in range(x+1,n-1):
                for z in range(y+1,n):
                    if nums[y] - nums[x] > diff or nums[z] - nums[y] > diff:
                        break
                    if (nums[y]-nums[x]) == diff and nums[z]-nums[y] == diff:
                        count+=1
                        
        return count
        
