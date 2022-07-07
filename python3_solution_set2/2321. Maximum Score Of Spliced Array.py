##ss
class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        
        ## number will either be from nums1 or nums2
        prefix_sum = [0] + list(accumulate(nums1)) ## prefix sum of nums1
        pre = [0] + list(accumulate(nums2)) ## prefix sum of nums2
        
        ## finding max possible sum of nums1 after max of 1 operations
        @lru_cache(None)
        def find_ans1(indx,prev,used):
            if indx == len(nums1):
                return 0
            
            else:
                ans = 0
                if used == 1 and prev+1!=indx:
                    ans = max(ans, prefix_sum[-1] - prefix_sum[indx])
                    
                elif used == 1 and prev+1 == indx:
                    ans = max(ans, nums2[indx] + find_ans1(indx+1,prev+1,used))
                    ans = max(ans, prefix_sum[-1] - prefix_sum[indx])
                    
                elif used == 0:
                    ans = max(ans, nums1[indx] + find_ans1(indx+1,prev,used))
                    ans = max(ans, nums2[indx] + find_ans1(indx+1,indx,1))
                    
                return ans
            
        ## finding max possible sum of nums2 after max of 1 operations
        @lru_cache(None)
        def find_ans2(indx,prev,used):
            if indx == len(nums1):
                return 0
            
            else:
                ans = 0
                if used == 1 and prev+1!=indx:
                    ans = max(ans, pre[-1] - pre[indx])
                    
                elif used == 1 and prev+1 == indx:
                    ans = max(ans, nums1[indx] + find_ans2(indx+1,prev+1,used))
                    ans = max(ans, pre[-1] - pre[indx])
                    
                elif used == 0:
                    ans = max(ans, nums2[indx] + find_ans2(indx+1,prev,used))
                    ans = max(ans, nums1[indx] + find_ans2(indx+1,indx,1))
                    
                return ans
            
        return max(find_ans1(0,0,0), find_ans2(0,0,0))
        
