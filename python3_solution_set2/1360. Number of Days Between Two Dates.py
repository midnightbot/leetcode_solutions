import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        a = datetime.datetime.strptime(date1,'%Y-%m-%d')
        b = datetime.datetime.strptime(date2,'%Y-%m-%d')

        return abs(a-b).days
