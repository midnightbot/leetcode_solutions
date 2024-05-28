class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        q = []
        nums = Counter(nums)
        for i in nums:
            if nums[i]==2:
                q.append(i)

       
        return reduce(lambda x, y: x ^ y, q) if len(q)>0 else 0

        
