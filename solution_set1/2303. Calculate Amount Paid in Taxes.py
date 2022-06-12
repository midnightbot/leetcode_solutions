##ss
class Solution:
    def calculateTax(self, b: List[List[int]], income: int) -> float:
        
        tax = 0
        
        curr = income
        indx = 0
        brackets = []
        brackets.append(b[0])
        
        for x in range(1,len(b)):
            brackets.append([b[x][0]-b[x-1][0],b[x][1]])
            
        #print(b)
        while curr!=0:
            
            if brackets[indx][0] <= curr:
                tax += brackets[indx][0] * (brackets[indx][1]) / 100
                curr-= brackets[indx][0]
                indx+=1
                
            else:
                tax += curr * (brackets[indx][1]) / 100
                curr = 0
                indx+=1
            #print(tax,curr)
        return tax
