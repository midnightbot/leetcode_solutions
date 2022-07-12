class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        temp = "0123456789abcdef"
        ans = ""
        for x in range(8):
            a = num & 15
            b = temp[a]
            ans = b + ans
            num = num >> 4
        return ans.lstrip('0')
        
