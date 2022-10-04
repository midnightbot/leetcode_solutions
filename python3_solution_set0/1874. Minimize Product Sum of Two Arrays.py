class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        
        temp1 = sorted(nums1, reverse=True)
        temp2 = sorted(nums2)
        
        temp3 = sorted(nums1)
        temp4 = sorted(nums2, reverse=True)
        
        ans1=0
        ans2=0
        for x in range(len(nums1)):
            ans1+=temp1[x]*temp2[x]
            ans2+=temp3[x]*temp4[x]
            
        return ans1
