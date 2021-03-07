class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        for x in range(len(arr)-2):
            temp1 = x+1
            temp2 = x+2
            if arr[x]%2!=0 and arr[temp1]%2!=0 and arr[temp2]%2!=0:
                return True
            
        return False
        
