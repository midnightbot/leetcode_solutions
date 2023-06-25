class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        count = 0
        nums = [str(x) for x in nums]

        for x in range(len(nums)):
            for y in range(x+1, len(nums)):
                if gcd(int(nums[x][0]), int(nums[y][-1])) == 1:
                    count+=1

        return count
