##ss
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        comp1 = set(nums1)
        comp2 = set(nums2)
        
        return [comp1.difference(comp2), comp2.difference(comp1)]
        
