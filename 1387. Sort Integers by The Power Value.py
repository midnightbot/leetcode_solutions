class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        ans = {}
        for x in range(lo,hi+1,1):
            count=0
            temp = x
            while temp!=1:
                count+=1
                if temp%2==0:
                    temp = int(temp/2)
                else:
                    temp = 3*temp + 1
                    
            ans[x] = count
            
        kk = sorted(ans.items(), key=operator.itemgetter(1))
        print(kk)
        keys_list = list(kk)
        key = keys_list[k-1]
        #key_list = list(kk.keys())
        #key = key_list[0]
        #print(key_list)
        
        return key[0]
            
                
        
