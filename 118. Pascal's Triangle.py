class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        ans = []
        if numRows == 1:
            ans.append([1])
            return ans
        elif numRows == 2:
            ans.append([1])
            ans.append([1,1])
            return ans
        elif numRows>=3:
            ans.append([1])
            ans.append([1,1])
           
            for x in range(2,numRows):
                temp = []
                for y in range(0,3+x-2):
                   
                    if y==0 or y==3+x-1-2:
                        temp.append(1)
                    else:
                        
                        temp.append(ans[x-1][y]+ans[x-1][y-1])
                    
                ans.append(temp)
            return ans   
            #print(ans)
            
            
        
        
