##ss
class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        
        ##win or not win
        
        @lru_cache(None)
        def ways(pos,arrows):
            
            if pos>=len(aliceArrows) or arrows == 0:
                return 0
            
            else:
                if arrows >= aliceArrows[pos] + 1:
                    #temp1 = ways(pos+1,arrows)
                    #temp2 = ways(pos+1,arrows - aliceArrows[pos])
                    ans = max(ways(pos+1,arrows), pos + ways(pos+1,arrows - aliceArrows[pos] - 1))
                    return ans
                else:
                    return ways(pos+1,arrows)
            
        points = ways(0,numArrows)
        #print(points)
        ##now try to make array with 'points' points
        self.ans = []
        def make_ans(pts, arrows,arr,indx):
            if pts == points:
                
                #print(arr)
                #print(self.ans)
                if arrows == 0:
                    self.ans.append(copy.deepcopy(arr))
                else:
                    arr[0]+=arrows
                    self.ans.append(copy.deepcopy(arr))
                #print(self.ans)
                #return arr
            
        
            elif arrows > 0 and indx < 12:
                if aliceArrows[indx]+1 <= arrows:
                    arr[indx] = aliceArrows[indx] + 1
                    make_ans(pts + indx, arrows - aliceArrows[indx] -1, arr, indx+1)
                    #print(arr)
                arr[indx] = 0
                make_ans(pts, arrows,arr,indx+1)
                
        make_ans(0,numArrows,[0 for x in range(12)],0)
        return self.ans[0]
        
        
