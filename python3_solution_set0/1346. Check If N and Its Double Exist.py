class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
    
      
    
        for x in range(len(arr)):
            if arr.count(2*arr[x])>=1 and arr[x]!=0:
                
                return True
            if arr[x] == 0 and arr.count(0)>=2:
                return True
     
        return False
