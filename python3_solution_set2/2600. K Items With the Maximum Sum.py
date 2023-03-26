class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        arr = [1 for x in range(numOnes)] + [0 for x in range(numZeros)] + [-1 for x in range(numNegOnes)]

        return sum(arr[:k])



