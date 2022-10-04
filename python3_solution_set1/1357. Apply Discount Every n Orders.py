##ss
class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.count = 0
        self.discount = discount
        self.price = {}
        self.n = n
        for x in range(len(products)):
            self.price[products[x]] = prices[x]
        #print(self.price)
    
    def getBill(self, product: List[int], amount: List[int]) -> float:
        
        self.count+=1
        
        total = 0
        for x in range(len(product)):
            total+=self.price[product[x]] * amount[x]
            
        if self.count%self.n == 0:
            return total * ((100-self.discount)/100)
        
        else:
            return total


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)
