##ss
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        l = 0
        while l + 1 < len(arr) and arr[l] <= arr[l+1]:
            l+=1
            
        if l == len(arr) - 1:
            return 0
        
        r = len(arr) - 1
        
        while r>l and arr[r-1] <= arr[r]:
            r-=1
        
        temp = min(len(arr) - l - 1, r)
        
        i = 0
        j = r
        
        while i <= l and j < len(arr):
            #print(i,j)
            if arr[j] >= arr[i]:
                temp = min(temp, j-i-1)
                
                i+=1
                
            else:
                j+=1
                
        return temp
                
        
