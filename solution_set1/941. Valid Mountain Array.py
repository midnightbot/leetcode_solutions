##ss
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        if len(arr) < 3:
            return False
        change = 0
        indx = -1
        for x in range(1,len(arr)):
            if arr[x] > arr[x-1] and change == 0:
                continue
                
            elif change == 0 and arr[x] <= arr[x-1]:
                indx = x
                change = 1
                
            elif change == 1 and arr[x] >= arr[x-1]:
                return False
            
            if arr[x] == arr[x-1]:
                return False
            
        rev_ord = sorted(arr, reverse = True)    
        return (change == 1 and rev_ord!=arr)
        
