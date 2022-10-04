class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        ans = []
        for x in range(len(matrix)):
            temp = []
            for y in range(len(matrix)):
                temp.append(matrix[x][y])
                
            ans.append(temp)
            
        ans = ans[::-1]
        #print(ans)
        #print(ans[2][0])
        for x in range(len(ans)):
            for y in range(len(ans)):
                #print(y,x,"hi",ans[y][x])
               
                matrix[x][y] = ans[y][x]
                
        #print(matrix)
            
        
        
