#ss
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits) == 0:
            ans  = []
            return ans
        arr = [int(digits[x]) for x in range(len(digits))]
        ans = []
        dicts = {}
        dicts[2] = ['a','b','c']
        dicts[3] = ['d','e','f']
        dicts[4] = ['g','h','i']
        dicts[5] = ['j','k','l']
        dicts[6] = ['m','n','o']
        dicts[7] = ['p','q','r','s']
        dicts[8] = ['t','u','v']
        dicts[9] = ['w','x','y','z']
        self.combinations(0,arr,ans,"",dicts)
        return ans
    
    def combinations(self,counter,arr,ans,temp,dicts):
        
        if counter < len(arr):
            y = len(dicts[arr[counter]])
            for x in range(y):
                self.combinations(counter+1,arr,ans,temp+dicts[arr[counter]][x],dicts)
                
        else:
            ans.append(temp)
            
        
            
            
        
        
