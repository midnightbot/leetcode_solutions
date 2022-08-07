##ss
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        
        ## j > i and j-i!=nums[j] - nums[i]
        ## j-nums[j]!=i-nums[i]
        count = 0
        n = len(nums)
        nums = [x-nums[x] for x in range(len(nums))]
        temp = Counter(nums)
        
        for x in temp:
            count+= temp[x] * (n-temp[x])
            
        return count//2
