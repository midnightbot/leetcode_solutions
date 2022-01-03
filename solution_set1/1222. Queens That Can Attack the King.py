##ss
class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        ans = set()
        ##check for queens in all 8 directions from king, as soon as one queen is found in a particular direction stop searching in that direction
        #print(queeni)
        ## ->
        for x in range(king[1],8):
            if [king[0],x] in queens:
                ans.add(tuple([king[0],x]))
                #queeni.remove(tuple([king[0],x]))
                break
                
        ## <-
        for x in range(king[1]-1,-1,-1):
            if [king[0],x] in queens:
                ans.add(tuple([king[0],x]))
                break
        
        ##down
        for x in range(king[0],8):
            if [x,king[1]] in queens:
                ans.add(tuple([x,king[1]]))
                break
                
        ##up
        for x in range(king[0]-1,-1,-1):
            if [x,king[1]] in queens:
                ans.add(tuple([x,king[1]]))
                break
                
        ##right diag down
        for x in range(8-max(king[0],king[1])+1):
            if [king[0]+x,king[1]+x] in queens:
                ans.add(tuple([king[0]+x,king[1]+x]))
                break
                
        ##right diag up
        for x in range(min(king[0],king[1])+1):
            if[king[0]-x,king[1]-x] in queens:
                ans.add(tuple([king[0]-x,king[1]-x]))
                break
                
        ##left diag down
        for x in range(min(8-king[0],king[1])+1):
            if [king[0]+x,king[1]-x] in queens:
                ans.add(tuple([king[0]+x,king[1]-x]))
                break
                
        ##left diag up
        for x in range(min(king[0],8-king[1])+1):
            if [king[0]-x,king[1]+x] in queens:
                ans.add(tuple([king[0]-x,king[1]+x]))
                break
        
        
        return ans
        
