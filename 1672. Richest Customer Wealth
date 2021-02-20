class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        print(len(accounts)) 
        print(len(accounts[0]))
        ans = [""]*len(accounts)
        total = 0
        for x in range(len(accounts)):
            total = 0
            for y in range(len(accounts[0])):
                total = total + accounts[x][y]
            ans[x] = total
            
        return max(ans)
                
        
