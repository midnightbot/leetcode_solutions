class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        
        ans = []
        
        for x in range(len(nums1)):
            if nums1[x] not in ans and  (nums1[x] in nums2 or nums1[x] in nums3):
                ans.append(nums1[x])
                
        for x in range(len(nums2)):
            if nums2[x] in nums3 and nums2[x] not in ans:
                ans.append(nums2[x])
                
        return ans
        
