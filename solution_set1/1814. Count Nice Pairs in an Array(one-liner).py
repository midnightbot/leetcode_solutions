##ss
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:

        return sum([comb(x,2)for x in Counter([x-int(str(x)[::-1]) for x in nums]).values()])%(10**9+7)
       
 
