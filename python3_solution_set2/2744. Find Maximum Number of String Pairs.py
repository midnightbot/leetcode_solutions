class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:

        rev = [x[::-1] for x in words]
        count = 0
        for x in range(len(words)):
            for y in range(x+1, len(words)):
                if words[x] == rev[y]:
                    count+=1

        return count
