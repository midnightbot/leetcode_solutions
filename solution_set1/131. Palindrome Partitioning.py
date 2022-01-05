##ss
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        self.result = []
        ans = []
        pointer = 0
        self.expand(s,0,ans)
        return self.result
    def expand(self,s,pointer,ans):
        #print(ans,pointer)
        if pointer == len(s):
            self.result.append(ans)
         
        
        if pointer < len(s):  
            for x in range(pointer,len(s)+1):
                temp = s[pointer:x]
                if temp!="" and temp == temp[::-1]:
                    new_ans = copy.copy(ans)
                    new_ans.append(temp)
                    self.expand(s,x,new_ans)
        
