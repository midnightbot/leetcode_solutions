##ss
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        temp1 = 0
        temp2 = 0
        count = 0
        for x in range(len(num1)-1,-1,-1):
            temp1 += int(num1[x]) * pow(10,count)
            count+=1
            
        count = 0
        for x in range(len(num2)-1,-1,-1):
            temp2 += int(num2[x]) * pow(10,count)
            count+=1
            
        return str(temp1+temp2)
        
