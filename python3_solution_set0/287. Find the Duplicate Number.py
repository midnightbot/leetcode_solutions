class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        ans = []
        for x in nums:
            if x not in ans:
                ans.append(x)
            else:
                return x
