##ss
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        nums2 = copy.deepcopy(nums)
        nums2 = sorted(nums)
        
        
        points = {'start':-1,'end':-1}
        
        for x in range(len(nums)):
            if nums[x]!=nums2[x]:
                if points['start'] == -1:
                    points['start'] = x
                points['end'] = x
            
        
        return points['end'] - points['start'] + 1 if points['start']!=-1 else 0
            
        
