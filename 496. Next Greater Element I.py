class Solution:
    def findComplement(self, num: int) -> int:
        ans = self.complement(num)
        return ans
        
        
    def complement(self,num):
        temp = format(num,"b")
        print(type(temp))
        ans = []
        #return temp
        for x in range(len(temp)):
            print(temp[x])
            if temp[x] == "0":
                ans.append(1)
                
            else:
                ans.append(0)
        print(ans)
        ans = ans[::-1]
        sums = 0
        #print(pow(2,0))
        for x in range(len(ans)):
            
            sums+=pow(2,x)*ans[x]
            print(sums)
        #print(sums)
        return sums
        #p
        
