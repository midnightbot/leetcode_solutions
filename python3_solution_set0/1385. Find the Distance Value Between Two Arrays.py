class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        ans = 0
        kk = []
        for x in range(len(arr1)):
            ans = 0
            for y in range(len(arr2)):
                if abs(arr1[x]-arr2[y])>d:
                    ans+=1
                    
                
            if ans == len(arr2):
                kk.append(arr1[x])
                    
                
                    
        return len(kk)
