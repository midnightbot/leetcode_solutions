class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        ## simple line sweep problem
        ## find max overlapping sets with atleast 1 ele in common

        n = max(nums)
        line = [0 for x in range(n+2)]

        for num in nums:
            start = max(num-k,0)
            end = min(num+k+1, n)
            line[start]+=1
            line[end]-=1
        
        ans = 1
        curr = 0
        for x in line:
            curr+=x
            ans = max(ans, curr)
        return ans
        
