##ss
class Solution:
    def numberOfDays(self, year: int, month: int) -> int:
        
        ans = [-1,31,28,31,30,31,30,31,31,30,31,30,31]
        
        #print(str(year)[-2:])
        if ((str(year)[-2:]!='00' and year%4==0) or (str(year)[-2:]=='00' and year%400==0)) and month == 2:
            return ans[2] + 1
        
        else:
            return ans[month]
        
