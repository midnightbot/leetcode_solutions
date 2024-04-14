class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        return bisect.bisect_left(list(accumulate(sorted(capacity, reverse=True))), sum(apple)) + 1

