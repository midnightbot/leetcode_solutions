class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        arr1 = [0 for x in range(26)]
        arr2 = [0 for x in range(26)]

        for x in range(len(s)):
            arr1[ord(s[x]) - ord('a')] = x
            arr2[ord(t[x]) - ord('a')] = x

        return sum([abs(arr1[x]-arr2[x]) for x in range(26)])
        
