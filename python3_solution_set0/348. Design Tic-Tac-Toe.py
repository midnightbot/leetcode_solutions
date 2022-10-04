##ss
class TicTacToe:
    moves = 0
    def __init__(self, n: int):
        self.queue = [[-1 for x in range(n)]for y in range(n)]
        self.moves = 0
        

    def move(self, row: int, col: int, player: int) -> int:
        
        self.moves+=1
        #print(self.moves)
        self.queue[row][col] = player
        
        ans = self.winning(row,col,player)
        if ans == -1:
            return 0
        else:
            return ans
            
        
        
        
        
            
        
    def winning(self,row,col,player):
        
        compare1 = [player  for x in range(len(self.queue))]
        #print(compare1)
        
        if self.queue[row] == compare1:
            return player
            
        for x in range(len(compare1)):
            if self.queue[x][col]!=self.queue[0][col]:
                break
                
        if x == len(compare1)-1 and self.queue[len(compare1)-1][col] == self.queue[0][col]:
            return player
        
        
        for x in range(len(self.queue)):
            if self.queue[x][x] != self.queue[0][0]:
                break
          
        if x == len(self.queue)-1 and self.queue[len(self.queue)-1][len(self.queue)-1] == self.queue[0][0]:
            return self.queue[0][0]
        
        for x in range(len(self.queue)):
            if self.queue[x][len(self.queue)-1-x] != self.queue[0][len(self.queue)-1]:
                break
                
        if x == len(self.queue)-1 and self.queue[len(self.queue)-1][0] == self.queue[0][len(self.queue)-1]:
            return self.queue[0][len(self.queue)-1]
        
        
        return -1


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
