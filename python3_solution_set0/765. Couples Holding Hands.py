class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        
        
        counter = 0
        
        for x in range(0,len(row),2):
            
            if row[x]%2==0 and row[x+1]!=row[x]+1:
                ind = row.index(row[x]+1)
                temp = row[x+1]
                row[x+1] = row[ind]
                row[ind] = temp
                counter+=1
      
            elif row[x]%2!=0 and row[x+1]!=row[x]-1:
                ind = row.index(row[x]-1)
                temp = row[x+1]
                row[x+1] = row[ind]
                row[ind] = temp
                counter+=1
                
        return counter
                        
