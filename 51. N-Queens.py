##ss
import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        final_ans = []
        ans = [-1 for x in range(n)]
        ##ans[i] contains column of ith queen, row will be i
        ##row,column,diagonal
        ##simple backtracking
        ##consider placing of queens in rows
        ##I am filling the queens row by row
        ##that is placing Queen in row0, then placing queens in all possible locations of row1, and so on
        
        #print(ans)
        aval_pos = [[x for x in range(n)] for y in range(n)]
        #print(aval_pos)
        
        for x in range(n):
            #print("inside")
            ans[0] = x
            #print(ans)
            new_upd_avl = self.upd_avl(0,x,aval_pos,n)
            ##new_upd_avl[x] gives which all columns Queen in row 'x' can be placed
            #print("called")
            self.expand(1,ans,new_upd_avl,final_ans,n)
            #print("finished")
            
        #print(final_ans)
        ret_ans = []
        
        for x in range(len(final_ans)):
            temp = ["" for x in range(n)]
            #print(temp)
            for y in range(len(final_ans[x])):
                loc = final_ans[x][y]
                strs = ""
                for z in range(loc):
                    strs+="."
                    
                strs+="Q"
                
                for z in range(loc+1,n):
                    strs+='.'
                    
                temp[y] = strs
                
            ret_ans.append(temp)
            
        return ret_ans

        
        
    def upd_avl(self,row,col,ans,n): 
        #print("inside")
        aval_pos =copy.deepcopy(ans)
        
        for x in range(row+1,n):##avoiding same column
            #print(x)
            if col in aval_pos[x]:
                aval_pos[x].remove(col)
                
            
        ##right diagonal
        ##right diagonal points will be (x+1,y+1)
        new_x = row+1
        new_col = col+1
        while new_x < n and new_col <n:
            if new_col in aval_pos[new_x]:
                aval_pos[new_x].remove(new_col)
                
            new_x+=1
            new_col+=1
            
        
        ##left diagonal
        ##left diagonal points will be (x+1,y-1)
        new_x = row+1
        new_col = col-1
        
        while new_x < n and new_col>=0:
            if new_col in aval_pos[new_x]:
                aval_pos[new_x].remove(new_col)
                
            new_x+=1
            new_col-=1
                
        return aval_pos
            
        
    def expand(self,curr,ans,aval_pos,final_ans,n):
        #print(curr,ans)
        
        if curr == n and ans.count(-1) == 0: ## 1 combination found, append it into final ans
            final_ans.append(ans)
            
            
        elif curr < n:
            for x in range(len(aval_pos[curr])): ##placing the queen in all possible columns of current row and recursively calling the function to fill queen in next row
                new_ans = copy.copy(ans)
                new_ans[curr] = aval_pos[curr][x]
                new_aval_pos = self.upd_avl(curr,aval_pos[curr][x],aval_pos,n)
                
                self.expand(curr+1,new_ans,new_aval_pos,final_ans,n)
        
        
        
        
        
