class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        ## simple dp Solution
        ## a number will either be taken or not be taken
        ## if it is taken sum%3 can  be 0,1,2

        ans = [0,0,0]

        for x in nums:
            c1 = ans[0] + x
            c2 = ans[1] + x
            c3 = ans[2] + x

            ans[c1%3] = max(ans[c1%3], c1)
            ans[c2%3] = max(ans[c2%3], c2)
            ans[c3%3] = max(ans[c3%3], c3)

        return ans[0]
        
