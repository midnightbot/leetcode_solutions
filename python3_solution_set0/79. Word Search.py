##ss
import copy
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ans = []
        og_board = [[0 for x in range(len(board[0]))] for y in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):
                
                og_board[x][y] = board[x][y]
        ##horizontal and vertical connection
        for x in range(len(board)):
            for y in range(len(board[0])):
                if len(ans)>=1:
                    return True
               
                if og_board[x][y] == word[0]:
                    #print("start")
                    new_b = [[0 for x in range(len(board[0]))] for y in range(len(board))]
                    for m in range(len(board)):
                        for n in range(len(board[0])):
                            new_b[m][n] = og_board[m][n]
                            
                    self.form_word(x,y,1,word,new_b,ans)
                        #ans.append(1)
                     
        if len(ans) >0:
            return True
        else:
            return False
        
    ##each subproblem will require a seperate board
    def form_word(self,m,n,chrs,word,board,ans):
        tempo = board[m][n]
        board[m][n] = -1
        #print(board,chrs)
        if chrs == len(word):
            #print("hi answer true")
            ans.append(1)
            return 
        #new_b = self.create_copy(board)
        if m+1 < len(board) and board[m+1][n] == word[chrs]:
            #print("part1")
            
            self.form_word(m+1,n,chrs+1,word,board,ans)
            
        if m-1>=0 and board[m-1][n] == word[chrs]:
            #print("part2")
         
            self.form_word(m-1,n,chrs+1,word,board,ans)
            
        if n+1 < len(board[0]) and board[m][n+1] == word[chrs]:
            #print("part3")
           
            self.form_word(m,n+1,chrs+1,word,board,ans)
            
        if n-1>=0 and board[m][n-1] == word[chrs]:
            #print("part4")
          
            self.form_word(m,n-1,chrs+1,word,board,ans)
        board[m][n] = tempo
    
    def create_copy(self,arr):
        ans = [[0 for x in range(len(arr[0]))] for y in range(len(arr))]
        
        for x in range(len(arr)):
            for y in range(len(arr[0])):
                ans[x][y] = arr[x][y]
                
        return ans
