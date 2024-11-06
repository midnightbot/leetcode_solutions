class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        i,j = 0,0

        for x in range(len(commands)):
            if commands[x] == "LEFT":
                i-=1
            elif commands[x] == "RIGHT":
                i+=1
            elif commands[x] == "UP":
                j-=1
            else:
                j+=1

        return (j*n)+i
        
