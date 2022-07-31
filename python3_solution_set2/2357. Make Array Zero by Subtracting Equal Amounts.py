class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        t = set(nums)
        if 0 in t:
            t.remove(0)
            
        return len(list(t))
