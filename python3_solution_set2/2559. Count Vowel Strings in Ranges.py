class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        ## simple prefix sum question
        ## time complexity : O(n)
        ## space complexity : O(n)
        def conv(strs):
            if strs[0] in "aeiou" and strs[-1] in "aeiou":
                return 1
            else:
                return 0



        words = [conv(x) for x in words]
        words = [0] + list(itertools.accumulate(words))
        ## r+1 - l
        ans = []
        for x,y in queries:
            ans.append(words[y+1] - words[x])

        return ans
