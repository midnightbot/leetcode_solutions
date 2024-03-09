class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums1 = set()
        nums2 = set()

        for x in nums:
            if x not in nums1:
                nums1.add(x)
            elif x not in nums2:
                nums2.add(x)
            else:
                return False

        return True
        
