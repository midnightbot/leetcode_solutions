class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dicts = {}

        for x,y in nums1:
            if x in dicts:
                dicts[x]+=y
            else:
                dicts[x] = y


        for x,y in nums2:
            if x in dicts:
                dicts[x]+=y
            else:
                dicts[x] = y

        ans = [[x,dicts[x]] for x in dicts]
        ans = sorted(ans, key = lambda x:x[0])
        return ans
