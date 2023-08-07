class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        
        if purchaseAmount%5==0:
            purchaseAmount+=1
        spend = round(purchaseAmount/10)*10
        return 100 - spend
