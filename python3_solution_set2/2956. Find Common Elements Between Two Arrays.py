class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return [sum([1 for x in nums1 if x in set(nums2)]), sum([1 for x in nums2 if x in set(nums1)])]


        
