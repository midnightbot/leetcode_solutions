class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        for x in nums1:
            if x in nums2:
                return x

        a = nums1[0]
        b = nums2[0]

        if a < b:
            return 10*a+b
        else:
            return 10*b + a
