##ss
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr = sorted(arr)
        
        mins = float('inf')
        
        for x in range(len(arr)-1):
            mins = min(mins, arr[x+1]-arr[x])
            
            
        ans = set()
        
        for x in range(len(arr)-1):
            if arr[x+1]-arr[x] == mins:
                ans.add(tuple((arr[x],arr[x+1])))
         
        ans = sorted(ans)
        return ans
            
        
