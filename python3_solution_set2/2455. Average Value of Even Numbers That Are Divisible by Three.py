class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        return int(sum([x for x in nums if x%6==0])/len([x for x in nums if x%6==0])) if len([x for x in nums if x%6==0])!=0 else 0
        
