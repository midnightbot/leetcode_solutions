##ss
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        ## 'k' numbers sum upto 'n'
        ## 1-9 only used
        ## each number at most once
        
        ans = set()
        
        def make_combinations(res, k, sums):
            #print(res,k,sums)
            if sums < 0:
                return 
            
            elif k == 0 and sums == 0:
                #print("inside")
                res = tuple(sorted(list(res)))
                #print(res)
                ans.add(res)
                
            elif k == 0 and sums > 0:
                return
            elif k > 0 and sums> 0:
                for z in range(1,10):
                    if z not in res and sums - z>=0:
                        res.add(z)
                        make_combinations(res,k-1,sums-z)
                        res.remove(z)
                        
                        
        make_combinations(set(),k,n)
        return ans
                
        
