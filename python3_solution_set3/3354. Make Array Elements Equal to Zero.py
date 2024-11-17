class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        # for a start indx 'x' sum on left side should be equal to sum on right side to make it valid
        ans = 0
        pre_sum = [0]
        post_sum = [0]
        for x in nums:
            pre_sum.append(pre_sum[-1] + x)
        pre_sum = pre_sum[1:]
        for x in nums[::-1]:
            post_sum.append(post_sum[-1] + x)
        
        post_sum = post_sum[1:][::-1]

        for i, x in enumerate(nums):
            if x == 0:
                if pre_sum[i] == post_sum[i]:
                    ans+=2
                elif abs(pre_sum[i] - post_sum[i]) == 1:
                    ans+=1
        # print(pre_sum, post_sum)
        return ans

        
