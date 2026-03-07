class Solution:
    def find_fee(self, n: int) -> int:
        if n==1:
            return 1
        elif 2<= n <= 5:
            return 2*n
        else:
            return 3*n

    def lateFee(self, daysLate: List[int]) -> int:
        return sum([self.find_fee(x) for x in daysLate])
        
