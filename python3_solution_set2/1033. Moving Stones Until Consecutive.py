class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:

        ## simple question
        ## sort a,b,c  find diff betn (mid and middle) and (max and middle)
        ## sums = diff1 + diff2

        ## if sums == 2 then min_moves = 0 elif sums == 3 then min_moves == 1 else 2
        ## max_moves = sums - 2

        arr = [a,b,c]
        arr.sort()

        diff1 = arr[1] - arr[0]
        diff2 = arr[2] - arr[1]

        space1=diff1-1
        space2=diff2-1
        mins = 0
        maxs = 0

        if space1==0 and space2!=0:
            mins = 1
        elif space1!=0 and space2==0:
            mins = 1
        elif space1==0 and space2==0:
            mins = 0
        else:
            ## mins will either be 1 or 2
            ## put left stone on left of mid and right stone on right of mid mins==2
            ## put left stone on right of mid and space2==1 mins==1
            ## put right stone on left of mid and space1==1 mins==1

            mins = 2
            if space2==1 or space1==1:
                mins = 1
        maxs = space1 + space2
        return [mins, maxs] 
