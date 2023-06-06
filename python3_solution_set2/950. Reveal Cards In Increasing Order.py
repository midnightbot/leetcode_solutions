class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        ans = []
        deck.sort(reverse = True)
        for x in deck:
            ans = [x] + ans[-1:] + ans[:-1]
        return ans
