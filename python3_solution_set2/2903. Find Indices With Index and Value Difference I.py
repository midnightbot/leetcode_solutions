class Solution:
    def findIndices(self, nums: List[int], id: int, vd: int) -> List[int]:

        ans = []

        for x in range(len(nums)):
            for y in range(len(nums)):
                if abs(x-y) >= id and abs(nums[x] - nums[y]) >= vd:
                    ans.append((x,y))
                    break

        return ans[0] if len(ans) >= 1 else [-1,-1]
        
