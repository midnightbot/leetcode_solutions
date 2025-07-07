class Solution:
    def is_prime(self,x):
        if x==1:
            return False
        for i in range(2,x):
            if x%i==0:
                return False
        return True

    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        nums = Counter(nums)
        
        for x in nums:
            if self.is_prime(nums[x]):
                return True

        return False
        
