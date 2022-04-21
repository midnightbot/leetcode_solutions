##ss
class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        def ret_nei(x1,y1):
            ans = []
            
            all_pts = [(x1+1,y1), (x1-1,y1), (x1,y1+1), (x1,y1-1)]
            
            for x,y in all_pts:
                if 0<=x<len(mat) and 0<=y<len(mat[0]):
                    ans.append(mat[x][y])
                else:
                    ans.append(-1)
                    
        
            return ans
        
        def check(num,arr):
            
            for x in arr:
                if num <= x:
                    return False
                
            return True
        
        
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                neis = ret_nei(x,y)
                if check(mat[x][y],neis):
                    return [x,y]
                
                
        
        
