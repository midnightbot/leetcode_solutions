##ss
class Solution:
    def maximumNumberOfOnes(self, w: int, h: int, side: int, maxs: int) -> int:
        
        ## always place the ones at the extreme left positon
        ## in second rectagle place it the extremre right
        
        ## first place at the topmost pos
        ## in second rect place it at the downmost pos
        ##keep on repeating the above pattern
        
        def print_ans(ans):
            for x in range(len(ans)):
                print(ans[x])
                
        ans = [[0 for x in range(w)] for y in range(h)]
        
        rstart = 0
        for x in range(len(ans)):
            seq = [(rstart + (x%side)*side +z) for z in range(side)]
            c = 0
            for y in range(len(ans[0])):
                ans[x][y] = seq[c]
                c+=1
                c%=side
                
        temp = Counter([ans[i][j] for i in range(len(ans)) for j in range(len(ans[0]))])
                
        temp = sorted(temp.values(),reverse=True)
        return sum(temp[:maxs])
                
