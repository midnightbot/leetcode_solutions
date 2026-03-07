class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        temp = Counter(nums)
        ans = 0
        for x in nums:
            if temp[x]%k==0:
                ans+=x

        return ans
        
