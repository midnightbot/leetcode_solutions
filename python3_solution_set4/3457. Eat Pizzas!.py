class Solution:
    def maxWeight(self, pizzas: List[int]) -> int:
        # odd day gain max()[-1] weight
        # even day gain max()[-2] weight
        ans = 0

        pizzas.sort()

        days = len(pizzas)//4
        indx = len(pizzas) - 1
        
        for x in range(math.ceil(days/2)):
            ans+=pizzas[indx]
            indx-=1
        
        for x in range(days - math.ceil(days/2)):
            ans+=pizzas[indx-1]
            indx-=2


        return ans


        
