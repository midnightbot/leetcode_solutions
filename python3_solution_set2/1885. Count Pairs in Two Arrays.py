class Solution:
    def countPairs(self, nums1: List[int], nums2: List[int]) -> int:
        ## i < j
        ## nums1[i] + nums1[j] > nums2[i] + nums2[j]
        ## nums1[i] - nums2[i] > nums2[j] - nums1[j]
        ## (nums1[i] - num2[i]) + (nums1[j] - nums2[j]) > 0

        temp = [nums1[x] - nums2[x] for x in range(len(nums1))]
        temp.sort()

        ans = 0
        n = len(temp)
        for x in range(len(temp)):
            indx = bisect.bisect_left(temp, -temp[x] + 1)
            ans+=n - max(x+1, indx)

        return ans
