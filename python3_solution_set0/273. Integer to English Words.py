##ss
class Solution:
    def numberToWords(self, num: int) -> str:
        ## 10^9 constraint
        
        ## d,ddd,ddd,ddd maximum
        ## billion, million, thousand, hundreds
        if num == 0:
            return "Zero"
        self.vals = [["One Hundred","Two Hundred","Three Hundred","Four Hundred","Five Hundred","Six Hundred","Seven Hundred","Eight Hundred", "Nine Hundred"],["Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"],["One","Two","Three","Four","Five","Six","Seven","Eight","Nine"],]
        #t = self.give_this_ans(408)
        ans = ""
        n = len(str(num))
        steps = n // 3
        left = n % 3
        #if left!=0:
            #steps+=1
        split = []
        nums = str(num)
        
        start = len(nums) - 1
        for x in range(steps):
            split.append(nums[start-2:start+1])
            start-=3
            
        if left!=0:
            split.append(nums[0:left])
        
        tmps = []
        for x in range(len(split)):
            thisans = self.give_this_ans(split[x])
            if x == 1 and thisans!="":
                thisans+= " Thousand"
                
            if x == 2 and thisans!="":
                thisans+= " Million"
                
            if x == 3 and thisans!="":
                thisans+=" Billion"
            
            tmps.append(thisans)
            
        tmps = tmps[::-1]
        for x in range(len(tmps)):
            if tmps[x]!="":
                ans+=tmps[x] + " "
        
        ans = ans.rstrip()
        return ans
            
            
            
    def give_this_ans(self,nums): ## gives how many thousands
        
        temp = ""
        c = 0
        if len(nums) == 2 and nums[0] == "1":
            if nums[1] == "0":
                return "Ten"
            
            elif nums[1] == "1":
                return "Eleven"
            
            elif nums[1] == "2":
                return "Twelve"
            
            elif nums[1] == "3":
                return "Thirteen"
            
            elif nums[1] == "4":
                return "Fourteen"
                
            elif nums[1] == "5":
                return "Fifteen"
            
            elif nums[1] == "6":
                return "Sixteen"
            
            elif nums[1] == "7":
                return "Seventeen"
            
            elif nums[1] == "8":
                return "Eighteen"
            
            elif nums[1] == "9":
                return "Nineteen"
        
        elif len(nums) == 3 and nums[1] == "1":
            if int(nums[0])!=0:
                temp+= self.vals[0][int(nums[0])-1] + " "
            if nums[2] == "0":
                temp+= "Ten"
            
            elif nums[2] == "1":
                temp+= "Eleven"
            
            elif nums[2] == "2":
                temp+= "Twelve"
            
            elif nums[2] == "3":
                temp+= "Thirteen"
            
            elif nums[2] == "4":
                temp+= "Fourteen"
                
            elif nums[2] == "5":
                temp+= "Fifteen"
            
            elif nums[2] == "6":
                temp+= "Sixteen"
            
            elif nums[2] == "7":
                temp+= "Seventeen"
            
            elif nums[2] == "8":
                temp+= "Eighteen"
            
            elif nums[2] == "9":
                temp+= "Nineteen"
                
            temp = temp.rstrip()
            return temp
            
        for x in range(len(str(nums))):
            if str(nums)[x]!="0":
            
                temp+=self.vals[x+(3-len(str(nums)))][int(str(nums)[x])-1] + " "
  
        temp = temp.rstrip()
        return temp
        
        
