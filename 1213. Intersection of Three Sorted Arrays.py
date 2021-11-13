class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        ans = []
        for x in range(len(arr1)):
            if arr1[x] in arr2 and arr1[x] in arr3:
                ans.append(arr1[x])
        return ans
