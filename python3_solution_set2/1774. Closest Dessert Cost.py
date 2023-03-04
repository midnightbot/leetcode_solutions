class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        ## atmost two of each topping
        ## only one base
        ## one or more type of topping

        ans = {'diff':float('inf')}

        m = len(toppingCosts)

        ## simple recursion
        @cache  
        def find_ans(indx, left):
            if indx == m:
                return left

            else:
                if left < 0:
                    return left
                
                else:
                    ans = float('inf')

                    ## take this num
                    a = find_ans(indx+1, left - toppingCosts[indx])
                    if abs(a) < abs(ans):
                        ans = a
                    elif abs(a) == abs(ans):
                        ## because if two ans are same we want the lowest ans
                        ## lowest ans will be when left is max in that case
                        ans = max(ans, a)

                    ## take this num twice
                    b = find_ans(indx+1, left - (2*toppingCosts[indx]))
                    if abs(b) < abs(ans):
                        ans = b
                    elif abs(b) == abs(ans):
                        ans = max(ans, b)

                    ## do no take this num
                    c = find_ans(indx+1, left)
                    if abs(c) < abs(ans):
                        ans = c
                    elif abs(c) == abs(ans):
                        ans = max(ans, c)

                    return ans

        
        anss = []

        for x in baseCosts:
            anss.append(find_ans(0,target-x))

        anss = [[x,abs(x)] for x in anss]

        anss = sorted(anss, key = lambda x:(x[1],-x[0]))

        return target - anss[0][0]


