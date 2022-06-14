class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        
        ans = []
        indx = {}
        
        
        for x in range(len(pieces)):
            for y in range(len(pieces[x])):
                indx[pieces[x][y]] = x
                
        
        x = 0
        while x!=len(arr):
            
            curr = arr[x]
            if curr not in indx:
                return False
            indx_curr = indx[curr]
            
            temp = pieces[indx_curr]
            lens = len(temp)
            
            if arr[x:x+lens]!= temp:
                return False
            else:
                x+=lens
            
        return True
        
