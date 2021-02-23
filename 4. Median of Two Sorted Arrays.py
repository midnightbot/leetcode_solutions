class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        ans = []
        i=0
        j=0
        while(i<m and j<n):
            if nums1[i]<nums2[j]:
                ans.append(nums1[i])
                i=i+1
                
            else:
                ans.append(nums2[j])
                j=j+1
                
        while(i<m):
            ans.append(nums1[i])
            i=i+1
            
        while(j<n):
            ans.append(nums2[j])
            j=j+1
            
        if((m+n)%2==0):
            kk=(m+n)/2
            return (ans[int(kk)]+ans[int(kk-1)])/2
        else:
            return ans[int((m+n)/2)]
            
        
