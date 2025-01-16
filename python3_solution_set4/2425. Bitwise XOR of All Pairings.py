from functools import reduce
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1 = len(nums1)
        len2 = len(nums2)
        # if a number will be present even number of times it will become 0
        # so check size of both arrays and find if a number will be present even number of times
        if len1%2==0 and len2%2==0:
            return 0
        elif len1%2==0 and len2%2!=0:
            return reduce(lambda x,y:x^y, nums1)
        elif len1%2!=0 and len2%2==0:
            return reduce(lambda x,y:x^y, nums2)
        else:
            return reduce(lambda x,y:x^y, nums1+nums2)
