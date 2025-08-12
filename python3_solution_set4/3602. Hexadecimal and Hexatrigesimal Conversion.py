class Solution:
    def to_base_36(self,num):
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while num:
            num, remainder = divmod(num, 36)
            result = digits[remainder] + result
        return result
    def concatHex36(self, n: int) -> str:
        
        return format(n**2, 'X') + self.to_base_36(n**3)
        
