##ss
import copy
import math
##in this solution I am trying to find out first character of the answer
##we can do the same procedure recursively and find 2nd 3rd...characters, hence improving the time complexity
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 1:
            return "1"
        
        if k == 1:
            temp = ""
            for x in range(n):
                temp+=str(x+1)
            return temp
        ans = []
        
        comp = math.factorial(n-1)
        #print(comp)
        t1 = k // comp
        t2 = k%comp
        
        if k%comp!=0:
            arr = [x+1 for x in range(n)]
            temp = arr.pop(t1)
            #print(arr)
            self.combinations(arr,ans,str(temp))
            ans = sorted(ans)
            return str(ans[t2-1])
        else:
            arr = [x+1 for x in range(n)]
            #temp = arr.pop(t1)
            #print(arr)
            self.combinations(arr,ans,"")
            ans = sorted(ans)
            return str(ans[k-1])
            
    def combinations(self,arr,ans,strs):
        
        if len(arr) == 0:
            ans.append(int(strs))
            
        else:
            for x in range(len(arr)):
                temp = arr.copy()
                temp.pop(x)
                self.combinations(temp,ans,strs+str(arr[x]))
                
        
