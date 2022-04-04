##ss
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        ## 'k' closest int to x
        
        ## simple, heap app
        
        arr = [[abs(arr[z] - x) , arr[z]] for z in range(len(arr))]
        
        arr = sorted(arr, key = lambda x:(x[0],x[1]))
        
        ans = [arr[x][1] for x in range(k)]
        ans = sorted(ans)
        return ans
