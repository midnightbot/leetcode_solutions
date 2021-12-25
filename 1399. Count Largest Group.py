##ss
class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        dicts = {}
        for x in range(1,n+1):
            temp = self.digit_sum(x)
            if temp in dicts.keys():
                dicts[temp]+=1
                
            else:
                dicts[temp] = 1
                
        ans = []
        for x in dicts.keys():
            ans.append([dicts[x],x])
            
        ans = sorted(ans,reverse = True, key = lambda x:x[0])
        count = 1
        for x in range(1,len(ans)):
            if ans[x][0] == ans[0][0]:
                count+=1
            else:
                break
                
        return count
    def digit_sum(self,n):
        
        temp = [int(x) for x in str(n)]
        return sum(temp)
        
