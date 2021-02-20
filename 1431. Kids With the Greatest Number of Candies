class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        str1 = []
        for candy in candies:
            newval = candy + extraCandies
            b = True
            for candy2 in candies:
                if newval < candy2:
                    b=False
            str1.append(b)
        return str1
