##ss
##Solution 1 (Time Limit Exceeded 127/136 test cases passed)
import copy
import math
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        
        rounds = 0
        
        ##consider all choices
        
        ##match between a,b a will win or b will win
        comp = [(x+1) for x in range(n)]
        #print(comp)
        self.mins = float('inf')
        self.maxs = -1
        self.play(comp,firstPlayer,secondPlayer,1)
        return [self.mins,self.maxs]
    
    def play(self, match, firstPlayer, secondPlayer,r):
        #print(match)
        
        if firstPlayer in match and secondPlayer in match:
            pairs = []

            for x in range(len(match)//2):
                pairs.append([match[x],match[-1 + -1*x]])
            #print(pairs)
            if [firstPlayer,secondPlayer]  in pairs or [secondPlayer,firstPlayer] in pairs:
                self.mins = min(self.mins,r)
                self.maxs = max(self.maxs,r)
                return 

            else:
                if len(match)%2!=0:
                    extra = match[len(match)//2]


                options = pow(2,len(pairs))
                for x in range(options):
                    thisresult = self.make_bin(x,len(pairs))
                    nextround = []
                    for z in range(len(thisresult)):
                        if thisresult[z]=="0":
                            nextround.append(pairs[z][0])

                        else:
                            nextround.append(pairs[z][1])

                    if len(match)%2!=0:
                        nextround.append(match[len(match)//2])
                    nextround = sorted(nextround)
                    self.play(nextround,firstPlayer,secondPlayer,r+1)
                
    def make_bin(self,n,lens):
        
        ans = ""
        for x in range(lens):
            if n & (1<<x):
                ans+="1"
                
            else:
                ans+="0"
                
        return ans[::-1]
                
                
        
        
        
