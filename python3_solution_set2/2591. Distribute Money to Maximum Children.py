class Solution:
    def distMoney(self, money: int, children: int) -> int:

        ## atleast 1 dollar to every child
        ## no child get exact 4 dollar

        ## return number of children getting 8 dollar
        if money < children:
            return -1

        ans = 0

        left = money - children

        ## now try to give max number of children 7 more dollars

        i = 0
        while left and i < children:
            if left >= 7:
                left-=7
                ans+=1
                i+=1
            else:
                if left == 3 and i == children-1:
                    ans-=1
                    i+=1
                    left = 0
                elif left == 3 and i!=children-1:
                    i+=1
                    left = 0 
                else:
                    left = 0
        if left > 0:
            ans-=1
        return max(ans,0)
