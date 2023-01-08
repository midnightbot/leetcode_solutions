class Solution:
    def categorizeBox(self, l: int, b: int, h: int, mass: int) -> str:

        arr = []
        ans = ""
        if max(l,b,h)>=10000 or l*b*h >=10**9:
            arr.append("Bulky")
        if mass >= 100:
            arr.append("Heavy")
        if "Heavy" in arr and "Bulky" in arr:
            ans = "Both"
        if len(arr) == 0:
            ans = "Neither"
        if "Bulky" in arr and "Heavy" not in arr:
            ans = "Bulky"
        if "Heavy" in arr and "Bulky" not in arr:
            ans = "Heavy"

        return ans
         
