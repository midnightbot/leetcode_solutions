class Solution:
    def find_indx(self, start, dis):
        return (start+dis)%self.n

    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        self.n = len(nums)
        result = []

        for x in range(self.n):
            if nums[x] == 0:
                result.append(0)
            
            else:
                ans = self.find_indx(x, nums[x])
                result.append(nums[ans])

        return result
        
