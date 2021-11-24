from math import gcd
class Solution:
    def fractionAddition(self, expression: str) -> str:
        
        
        counter = 1
        temp = len(expression)
        
        while counter<temp: ##before every minus I am adding a + sign and then will split the string on plus sign
            #print(expression)
            if expression[counter] == '-':
                expression = expression[0:counter]+"+"+expression[counter:temp]
                counter+=1
                temp+=1
            counter+=1
            
        strs = expression.split('+')  ## splitting the string on plus sign
        print(strs)
        num = []
        deno = []
        
        for x in range(len(strs)): ## converting the splitted string into numerator and denominator
            #strs[x] = float(strs[x])
            
            lens = strs[x].split('/')
            num.append(int(lens[0]))
            deno.append(int(lens[1]))
            
        denos = 1
        for x in range(len(deno)): ##finding the multiplication of denominators
            denos *= deno[x]
           
        sums = 0
        #print(num,deno)
        for x in range(len(num)): ## multiplying the common denominator with all numerators
            #print(denos)
            num[x]*= (denos//deno[x])
            
        #print(num,deno)   
        numerator = sum(num) ## final numerator is sum of all numerators as all numerators all multiplied by common denominator and the string is split on + sign hence add num array
        ##deno is the common denomintor
        ##now answer is found, just reduce it to lowest form
        
        a,b = self.reducefraction(numerator,denos)
        
        ans = ""
        ans = str(a)+"/"+str(b)
        return ans
        
        
    def reducefraction(self,x,y): ## function to reduce fractiont to lowest form
        
        d = gcd(x,y)
        x = x//d
        y = y //d
        
        return x,y
        
        
            
        
            
        
