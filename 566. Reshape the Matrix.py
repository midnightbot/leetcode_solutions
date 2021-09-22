class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        ans = [-1]*len(mat)*len(mat[0])
        counter = 0
        if r*c != len(mat)*len(mat[0]):
            return mat
        
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                ans[counter] = mat[x][y]
                counter+=1
        if r==1:
            ret_ans = []
            ret_ans.append(ans)
            return ret_ans
        elif c==1:
            ret_ans = []
            for z in range(len(ans)):
                temp = []
                temp.append(ans[z])
                ret_ans.append(temp)
            return ret_ans
        
        else:
            ret_ans = []
            for z in range(r):
                temp = []
                for m in range(z*c, z*c+c):
                    temp.append(ans[m])
                ret_ans.append(temp)
            return ret_ans
        
