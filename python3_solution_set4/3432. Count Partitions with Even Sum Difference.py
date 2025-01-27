class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        pre_sum = list(accumulate(nums))
        ans = 0
        for x in range(0,len(nums)-1):
            a = pre_sum[x]
            b = pre_sum[-1] - pre_sum[x]
            if (a-b)%2==0:
                ans+=1
        return ans

        
