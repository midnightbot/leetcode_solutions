class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:

        return s == "".join([x[0] for x in words])
