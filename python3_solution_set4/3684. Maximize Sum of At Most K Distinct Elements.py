class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(list(set(nums)), reverse=True)
        return nums[:min(len(nums),k)]
        
