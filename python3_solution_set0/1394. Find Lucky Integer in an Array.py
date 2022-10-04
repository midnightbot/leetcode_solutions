class Solution:
    def findLucky(self, arr: List[int]) -> int:
        
        count = 0
        ans = []
        ans.append(-1)
        for x in range(len(arr)):
            temp = arr[x]
            for y in range(len(arr)):
                
                if arr[y]==arr[x] and y!=x:
                    count+=1
                    
            if temp-1==count:
                ans.append(temp)
                
            count = 0
            
        return max(ans)
                
