class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        ans = []
        
        for x in range(len(arr)):
            counts = arr.count(arr[x])
            ans.append(counts)
            
        counter = 0
        for x in range(len(ans)):
            
            if ans[x] == 1:
                counter+=1
                
            if counter == k:
                return arr[x]
            
        return ""
        
