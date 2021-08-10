import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def reset(self) -> List[int]:
        return self.nums
        """
        Resets the array to its original configuration and return it.
        """
        

    def shuffle(self) -> List[int]:
        result = []
        result = self.nums[:]
        random.shuffle(result)
        return result
        
        """
        Returns a random shuffling of the array.
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
