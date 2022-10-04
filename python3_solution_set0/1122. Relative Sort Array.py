class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for x in range(len(arr2)):
            for y in range(len(arr1)):
                if arr2[x] == arr1[y]:
                    ans.append(arr1[y])
                    
        x =0
        for x in range(len(ans)):
            if ans[x] in arr1:
                arr1.remove(ans[x])
                
        arr1 = sorted(arr1)
        x=0
        for x in arr1:
            ans.append(x)
            
        return ans
            
                
      
        
