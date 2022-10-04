class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr = sorted(arr)
        diff = arr[1] - arr[0]
        count = 0
        for x in range(len(arr)-1):
            if arr[x+1]-arr[x] == diff:
                count+=1
            else:
                return False
            
        if count==len(arr)-1:
            return True
        else:
            return False
                
        
