class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        
        if len(matrix) == 0:
            return 0
        ####################################
        for x in range(len(matrix[0])):## converting first row into integer
            matrix[0][x] = int(matrix[0][x])
        #######################################  
        for x in range(1,len(matrix)):
            for y in range(len(matrix[0])):
                if int(matrix[x][y])!=0:
                    matrix[x][y] = 1 + matrix[x-1][y]
                else:
                    matrix[x][y] = 0
                    
        ########################################           
        ans  = 0
        #print(matrix)
        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y]!=0:
                    ans = max(ans, matrix[x][y])
                    for z in range(y+1,len(matrix[0])):
                        if matrix[x][z]!=0:
                            #print((z-y)*min(matrix[x][y:z+1]))
                            ans = max(ans, (z-y+1)*min(matrix[x][y:z+1]))
                            
                        else:
                            break
        #########################################                    
        return ans
        
        
