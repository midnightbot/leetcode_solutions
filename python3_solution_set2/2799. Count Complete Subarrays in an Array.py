class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        
        k = len(set(nums))
        ans = 0
        n = len(nums)
        for x in range(len(nums)):
            seenset = set()
            for y in range(x,len(nums)):
                seenset.add(nums[y])
                if len(seenset) == k:
                    ans+= (n-y)
                    break
                


        return ans
