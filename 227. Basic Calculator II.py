##ss
class Solution:
    def calculate(self, s: str) -> int:
        
        s = s.replace(" ","") ##removing all blank spaces
        #print(s)
        temp = []
        nums = ""
        for x in range(len(s)):
            #print(temp)
            if ord(s[x]) >=48 and ord(s[x])<=57:
                nums+=s[x]
                
            else:
                temp.append(int(nums))
                temp.append(s[x])
                nums = ""
           
        ##mul and div left to right
        
        temp.append(int(nums))
        #print(temp)
        while temp.count('*')!=0 or temp.count('/')!=0:
            #print(temp)
            for x in range(len(temp)):
                if temp[x] == "*" or temp[x] == "/":
                    break
                    
            op = temp[x]
            
            if op == '*':
                ans = temp[x-1] * temp[x+1]
                
            else:
                ans = temp[x-1] // temp[x+1]
            #print(ans)  
            temp.insert(x-1,ans)
            #print(temp,x)
            temp = temp[0:x] + temp[x+3:len(temp)]
            #print(temp)
           
        #print(temp)
        ##only + - operations are left now
        print(temp)
        ans = 0
        ans+=temp[0]
        
        for x in range(1,len(temp)):
            if type(temp[x]) == int and temp[x-1] == "+":
                ans+=temp[x]
                
            elif type(temp[x]) == int and temp[x-1] == '-':
                ans-=temp[x]
                
        return ans
            
            
        
