class Solution:
    def convertDateToBinary(self, date: str) -> str:
        date = date.split("-")
        date = [format(int(x),'b') for x in date]
        return "-".join(date)
        
