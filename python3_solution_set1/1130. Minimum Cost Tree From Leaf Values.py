##ss
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        ##0 or 2 children
        ## none left val = largest right tree leaf * largest ritgh tree leaf
        
        
        ##arr is in inorder traversal hence no shuffling is requried
        
        @lru_cache(None)
        def find_ans(i,j):
            
            
            
            if i >= j:
                return 0
            
            else:
                ans = float('inf')
                for z in range(i+1,j+1):
                    ans = min(ans, max(arr[i:z]) * max(arr[z:j+1]) + find_ans(i,z-1) + find_ans(z,j))
                return ans
            
                
        return find_ans(0,len(arr)-1)
