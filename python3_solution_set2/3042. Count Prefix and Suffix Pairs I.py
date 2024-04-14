class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1,str2):
            n = len(str1)
            return str1 == str2[:n] and str1 == str2[-n:]
        ans = 0
        for x in range(len(words)):
            for y in range(x+1,len(words)):
                if isPrefixAndSuffix(words[x],words[y]):
                    ans+=1
        return ans
