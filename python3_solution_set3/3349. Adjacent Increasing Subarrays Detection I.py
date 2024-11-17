class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        # sliding window of size k
        is_valid = {}

        for x in range(len(nums)-k+1):
            temp = nums[x:x+k]
            if temp == sorted(temp) and len(set(temp)) == k:
                is_valid[x] = True
            else:
                is_valid[x] = False
    
        for x in is_valid:
            if x+k in is_valid and is_valid[x] and is_valid[x+k]:
                return True

        return False
        
