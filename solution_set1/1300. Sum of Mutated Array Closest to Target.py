##ss
class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        
        def find_val(val):
            return sum([min(x,val) for x in arr])
        
        arr = sorted(arr)
        #print(arr)
        
        l = 0
        r = max(arr)
        
        while l < r:
            mid = (l+r+1)//2
            
            if find_val(mid) < target:
                l = mid 
                
            else:
                r = mid - 1
                
            #print(find_val(mid), mid, l, r)
            
        ##now check l,l-1,l+1
        
        while l < r:
            mif 
        comp = [[abs(find_val(l)-target),l], [abs(find_val(l-1) - target),l-1], [abs(find_val(l+1) - target),l+1]]
        comp.sort()
        return comp[0][1]
