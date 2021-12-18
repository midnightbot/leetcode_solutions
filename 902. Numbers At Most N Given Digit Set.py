##Solution 1(TIme Limit Exceeded) 82/84 Testcases passed
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        ans = []
        count = 0
        if len(str(n)) == 1:
            anss = 0
            #print("hello")
            for x in range(len(digits)):
                if int(digits[x]) <=n:
                    
                    anss+=1
                else:
                    break
                    
            return anss
        
        if len(str(n)) >=2:
            for x in range(len(str(n))-1):
                #print(count)
                count+=pow(len(digits),x+1)
            
            if int(digits[len(digits)-1]) < int(str(n)[0]):
                count+=pow(len(digits),len(str(n)))
                return count
            
            elif int(digits[len(digits)-1]) < int(str(n)[0]):
                for x in range(len(digits)):
                    self.counts(digits,n,ans,digits[x],len(str(n))-1)
                return len(ans) + count
            
            else:
                
                for x in range(len(digits)):
                    if int(digits[x]) < int(str(n)[0]):
                        count+=pow(len(digits),len(str(n))-1)

                    elif int(digits[x]) == int(str(n)[0]):
                        #print("hi")
                        self.counts(digits,n,ans,digits[x],len(str(n))-1)
                        return count + len(ans)

                    else:
                        return count

    def counts(self,digits,n,ans,curr,size):
        
        if size == 0 and int(curr)<=n:
            ans.append(1)
            
        else:
            
            for x in range(len(digits)):
                if int(curr+str(digits[x])) <= n:
                    self.counts(digits,n,ans,curr+str(digits[x]),size-1)
                    
                else:
                    break
     
     
     
##Solution 2
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        
        if len(str(n)) == 1:
            c = 0
            for x in range(len(digits)):
                if int(digits[x]) <= n:
                    c+=1
                    
            return c
        temp1 = self.lessdigits(digits,n)
        #print(temp1)
        temp2 = self.samedigits(digits,n)
        return temp1+temp2
        
    def lessdigits(self,digits,n):
        
        ans = 0
        for x in range(1,len(str(n))):
            ans+=pow(len(digits),x)
        
        return ans
            
        
    def samedigits(self,digits,n):
        
        ans = 0
        for x in range(len(str(n))):
            count = 0
            for y in range(len(digits)):
                if int(digits[y]) < int(str(n)[x]):
                    count+=1
                    
                else:
                    break
                    
            ans+=(count) * pow(len(digits),len(str(n))-x-1)
            
            #print(str(n)[x] in digits)
            if (str(n)[x] not in digits):
                break
                
        
        #print(x)
        ans+= (x==len(str(n))-1 and str(n)[len(str(n))-1] in digits)
        
        return ans
        
