class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self.withdraw(account1, money): 
            if self.deposit(account2, money): return True 
            self.deposit(account1, money)

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= len(self.balance): 
            self.balance[account-1] += money
            return True 
        
    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= len(self.balance) and self.balance[account-1] >= money: 
            self.balance[account-1] -= money
            return True 

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
