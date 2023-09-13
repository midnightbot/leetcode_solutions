class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = [0 for x in range(101)]

        for x,y in nums:
            for it in range(x,y+1):
                ans[it] = 1

        return ans.count(1)
        
