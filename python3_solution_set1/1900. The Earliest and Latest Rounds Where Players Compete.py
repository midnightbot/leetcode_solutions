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
                
                
        
        
        
##Solution 2
##same as Solution1, minor change instead of checking all 2^n options, put 1's on place of firstPlayer and secondPlayer and check for 2^(n-2) combinations as,
##if we do not have either of them in the next round, we will terminate it
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        
        ans = set()
        def play(players,rounds):
            
            if len(players) < 2:
                return 
            
            else:
                pairs = []
                for x in range(len(players)//2):
                    a = players[x]
                    b = players[-1-x]
                    
                    if a == firstPlayer and b == secondPlayer:
                        ans.add(rounds)
                        return 
                    
                    elif a!=firstPlayer and b!=secondPlayer and a!=secondPlayer and b!=firstPlayer:
                        pairs.append([a,b])
                        
                extra = [firstPlayer,secondPlayer]
                if len(players)%2!=0:
                    extra.append(players[len(players)//2])
                extra = tuple(set(extra))
                for nxt in product(*pairs):
                    play(sorted(nxt+tuple(extra)),rounds+1)
                    
        play([(x+1) for x in range(n)],1)
        return [min(ans),max(ans)]
                        
        
