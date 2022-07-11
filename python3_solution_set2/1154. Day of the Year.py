##ss
class Solution:
    def dayOfYear(self, date: str) -> int:
        count = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        
        year = int(date[0:4])
        mnth = int(date[5:7])
        dt = int(date[8:])
        ans = 0
        
        for d in range(1,mnth):
            if d == 2 and year%4==0 and (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
                ans+=1
                
            ans+= count[d]
            
            
        ans+=dt
        
        
        return ans
        #print(year,mnth,dt)
