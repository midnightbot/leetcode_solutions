##ss
class Solution:
    def intToRoman(self, num: int) -> str:
        
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
        
        
        ans = ""
        
        for x in range(len(digits)):
            if num == 0:
                break
                
            else:
                repeats = num // digits[x][0]
                num = num % digits[x][0]
                for y in range(repeats):
                    ans+=digits[x][1]

                
        return ans
        
