class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        ans = [None] * len(nums1)
        i =0 
        j= 0
        k= 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ans[k] = nums1[i]
                k+=1
                i+=1
                
            else:
                ans[k] = nums2[j]
                k+=1
                j+=1
                
        while i < m:
            ans[k] = nums1[i]
            k+=1
            i+=1
            
        while j < n:
            ans[k] = nums2[j]
            j+=1
            k+=1
            
        for x in range(len(ans)):
            nums1[x] = ans[x]
