import math
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        if len(arr) == 1:
            return arr[0]
        
        counter = 0
        n = int((len(arr)/4)+(1))
        print(n)
        while counter<len(arr)-n+1:
            if arr[counter] == arr[counter+n-1]:
                return arr[counter]
            else:
                counter+=1
                
        
        
