class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        
        ## [ ]
        ##bit at pos arr[i] is set to 1
        
        
        if m == len(arr):
            return m
        grps = [0 for x in range(len(arr) + 2)]
        
        result = -1
        
        for x in range(len(arr)):
           
            indx = arr[x]
            
            l = grps[indx-1]
            r = grps[indx+1]
            
            if l == m or r == m:
                result = x
                
            #print(grps)
            grps[indx-l] = grps[indx+r] = l + r + 1
            
        return result
            
            
                
            
        
