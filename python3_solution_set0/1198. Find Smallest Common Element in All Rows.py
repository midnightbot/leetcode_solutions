class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        
        ans = 0
        for x in range(len(mat)):
            mat[x].append(-1)
            
        #print(mat)
        mat.append([0])
        print(mat)
        for x in range(len(mat[0])):
            for y in range(len(mat)):
                
                if mat[0][x] not in mat[y]:
                    break
                    
                else:
                    ans = mat[0][x]
                    
            if ans!=0 and y==len(mat)-1:
                return ans
        
        return ans
