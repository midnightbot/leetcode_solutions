class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        ## each person owing money can give money to any other person

        temp = {}

        for x,y,amt in transactions:
            temp[x] = temp.get(x,0) - amt
            temp[y] = temp.get(y,0) + amt

        temp = [temp[x] for x in temp if temp[x]!=0]
        n = len(temp)

        def find_ans(indx):
            while indx < n and temp[indx] == 0: ## if the current person is settled move to the next person
                indx+=1 

            if indx == n:
                return 0

            ans = 10**9
            for x in range(indx+1, n): ## check if this person can settle debt for person at indx (they can settle debt if they have opposite sign of balances)
                if temp[indx] * temp[x] < 0:
                    temp[x] += temp[indx]
                    ans = min(ans, 1 + find_ans(indx+1))
                    temp[x] -= temp[indx]

            return ans

        return find_ans(0)
        
        
