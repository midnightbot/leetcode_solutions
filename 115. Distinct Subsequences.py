##ss
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        ##simple recursion with two branches
        ##we have two options either a bracket will be in optimal solution or not in optimal solution
        
        disp = self.find_removal_length(s) ## gives how many ( and ) are to be removed
        #print(left,right)
        self.ans = set()
        self.expand(s,0,disp[0],disp[1],"")
        ##left -> (
        ##right -> )
        return self.ans
    def find_removal_length(self,s):
        left = 0
        right = 0
        
        for x in range(len(s)):
            if s[x] == ")" and left >0:
                left-=1
                
            elif s[x] == ")" and left == 0:
                right+=1
                
            elif s[x] == "(":
                left+=1
                
        return [left,right]
    
    
    def expand(self,s,pointer,left,right,strs):
        #print(left,right,strs,pointer)
        
        if left + right <= len(s) - pointer: ## if left + right > len(s) - pointer then even if we remove all char from here we will not be able to make this combination valid
            
            if left == 0 and right == 0 and self.find_removal_length(strs+s[pointer:]) == [0,0]:## no more moves can be done
                self.ans.add(strs+s[pointer:])

            

            elif pointer < len(s) and left ==0 and right == 0: ## 
                new_s = copy.copy(strs)
                new_s+= s[pointer]
                self.expand(s,pointer+1,left,right,new_s)

            elif pointer < len(s) and (left>0 or right>0):
                #print(len(s))
                new_s = copy.copy(strs)
                #print(pointer)
                new_s+= s[pointer]
                self.expand(s,pointer+1,left,right,new_s) ## not removing the current character

                if s[pointer] == "(" and left>0: ##removing curr ( bracket
                    self.expand(s,pointer+1,left-1,right,strs)


                if s[pointer] ==")" and right >0: ## removing curr ) brakcet
                    self.expand(s,pointer+1,left,right-1,strs)

            
                
        
