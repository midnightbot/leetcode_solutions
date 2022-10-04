##ss
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        
        ## just change find_sum function
        
        presum = [[0 for x in range(len(mat[0]) + 1)] for y in range(len(mat) + 1)]
        #print(presum)
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                presum[x+1][y+1] = presum[x+1][y] + presum[x][y+1] - presum[x][y] + mat[x][y]
                
        def find_sum(x1,x2,y1,y2):
            side = abs(x2-x1)
            return presum[x2][y2] - presum[x2][y1] - presum[x1][y2] + presum[x1][y1]
        
        def check_sum(size):
            #print("size is", size)
            for x in range(len(mat) - size + 1):
                for y in range(len(mat[0]) - size + 1):
                    #print(x,"___",len(presum), size)
                    ans = find_sum(x,x+size,y,y+size)
                    #print(ans)
                    if ans <= threshold:
                        return True
                    
            return False
                
        
        l = 0
        r = min(len(mat), len(mat[0]))
        
        while l < r:
            mid = (l+r)//2 + 1
         
            if check_sum(mid):
                l = mid
                
            else:
                r = mid - 1
            
        return l
