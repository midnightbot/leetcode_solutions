class Solution:
    def kthCharacter(self, k: int) -> str:

        def find_next(s):
            ans = ""
            for i in s:
                ans+=chr(((ord(i)-ord('a')+1)%26)+ord('a'))
            return ans

        res = "a"
        while len(res) < k:
            res+=find_next(res)
        return res[k-1]
        
