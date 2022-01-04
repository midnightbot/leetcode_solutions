##ss
class Solution:
    def minFlips(self, target: str) -> int:
        
        ##number of groups of continuos ones and zeros will be the answer
        
        count = 0
        prev = "0"
        for x in range(len(target)):
            if target[x]!=prev:
                count+=1
                prev = target[x]
                
        return count
        
