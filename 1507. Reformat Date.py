##ss
class Solution:
    def reformatDate(self, date: str) -> str:
        
        temp = date.split(" ")
        month = [-1,"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        
        day = ""
        for x in range(len(temp[0])):
            if ord(temp[0][x])>=48 and ord(temp[0][x])<=57:
                day+=temp[0][x]
                
            else:
                break
                
        temp[0] = day
        if len(temp[0]) == 1:
            temp[0] = str('0')+temp[0]
            
        
        temp[1] = str(month.index((temp[1])))
        if len(temp[1]) == 1:
            temp[1] = str('0')+temp[1]
        ans = ""
        ans+=str(temp[2]) + "-" + str(temp[1])+"-"+str(temp[0])
        return ans
        
