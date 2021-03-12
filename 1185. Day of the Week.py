import datetime 
import calendar 
  
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date = str(day)+" "+str(month)+" "+str(year)
        born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
        
        return (calendar.day_name[born]) 
        
