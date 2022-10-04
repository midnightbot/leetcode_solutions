##ss
class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        ##bitwise subtraction using ones complement 
        ##link : https://byjus.com/maths/binary-subtraction/
        bina = self.getbinary(a)
        binb = self.getbinary(b)
        if a ==0:
            return b
        elif b ==0:
            return a
        if a*b > 0:
            if a > 0 and b > 0:
                bina = self.getbinary(a)
                binb = self.getbinary(b)
                carry,result = self.add(bina,binb)
                return self.getint(result)
            else:
                binsa = self.getbinary(-1*a)
                binsb = self.getbinary(-1*b)
                carry,result = self.add(binsa,binsb)
                return -1 * self.getint(result)
                
        else:
            if a>0 and b < 0:
                bina = self.getbinary(a)
                binb = self.getbinary(-1*b)
                carry,result = self.subs(bina,binb)
                temp = self.getint(result)
                if carry == 0:
                    temp = temp * -1
                return temp
            else:
                print("insidee")
                bina = self.getbinary(-1 * a)
                binb = self.getbinary(b)
                #print("inside",bina,binb)
                carry,result = self.subs(binb,bina)
                print(carry,result)
                temp = self.getint(result)
                print(temp)
                if carry == 0:
                    temp = temp * -1
                    
                return temp
            
        return self.getint(result)
        
     
    def add(self,bina,binb):
        carry = 0
        result = ""
        for x in range(len(bina)-1,-1,-1):
            if bina[x] == "1" and binb[x] == "1" and carry == 0:
                result+="0"
                carry = 1
                
            elif bina[x] =="1" and binb[x] == "1" and carry == 1:
                result+="1"
                carry = 1
                
            elif bina[x] == "1" and binb[x] == "0" and carry == 0:
                result+="1"
                carry = 0
                
            elif bina[x] == "1" and binb[x] == "0" and carry == 1:
                result+="0"
                carry = 1
                
            elif bina[x] == "0" and binb[x] =="1" and carry == 0:
                result+="1"
                carry  = 0
                
            elif bina[x] == "0" and binb[x] == "1" and carry == 1:
                result+="0"
                carry = 1
                
            elif bina[x] == "0" and binb[x] == "0" and carry ==0:
                result+="0"
                carry = 0
                
            elif bina[x] == "0" and binb[x] == "0" and carry == 1:
                result+="1"
                carry = 0
        return carry,result
    
    def subs(self,bina,binb):
        ##using ones comp
        newbinb = ""
        for x in range(len(binb)):
            if binb[x] == "0":
                newbinb+="1"
            else:
                newbinb+="0"
                
        carry,res = self.add(bina,newbinb)
        if carry == 0:
            print(carry,res)
            updres = ""
            for x in range(len(res)):
                if res[x] == "0":
                    updres+="1"
                else:
                    updres+="0"
                
            return 0,updres
        
        else:
            c,tempo = self.add(res[::-1],self.getbinary(1)) 
            return 1,tempo
    def getbinary(self,num):
        
        ans = ""
        for x in range(10):
            if num & 1 << x != 0:
                ans+="1"
                
            else:
                ans+="0"
                
        ans = ans[::-1]
        
        return ans
    
    
    def getint(self,nums):
        res = 0
        for x in range(len(nums)):
            res+= int(nums[x]) * pow(2,x)
            
        return res
            
        
