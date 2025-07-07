class Solution:
    def countOddLetters(self, n: int) -> int:
        maps = {
            0:"zero",
            1:"one",
            2:"two",
            3:"three",
            4:"four",
            5:"five",
            6:"six",
            7:"seven",
            8:"eight",
            9:"nine"
        }
        strs = ""

        for x in str(n):
            strs+=maps[int(x)]
        
        strs = Counter(strs)
        ans = 0

        for x in strs:
            if strs[x]%2!=0:
                ans+=1
        
        return ans
        
