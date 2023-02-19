from collections import Counter
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:

        dicts1 = Counter(basket1)
        dicts2 = Counter(basket2)
        ## either replace a pair
        ## or replace i with min and replace min back to arr
        dicts = dicts1 + dicts2

        mins = min(dicts)

        for it in dicts:
            if dicts[it]%2==1:
                return -1
            dicts[it]//=2

        dicts1-=dicts
        dicts2-=dicts

        arr = sorted(list(dicts1.elements()) + list(dicts2.elements()))
        #print(arr)
        return sum([min(2*mins, arr[x]) for x in range(len(arr)//2)])
        
