class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        balance = 0
        ans = []
        ## create a balance array
        ## all even balances in group A and odd balance in group B
        
        for x in range(len(seq)):
            if seq[x] == '(':
                balance+=1
                ans.append(balance)

            else:
                ans.append(balance)
                balance-=1

        ans = [x%2 for x in ans]
        return ans
