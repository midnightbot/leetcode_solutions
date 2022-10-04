##ss
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        self.ans = set()
        
        for x in range(len(emails)):
            self.process(emails[x])
            
            
        return len(list(self.ans))
        
        
    def process(self,email):
        
        parts = email.split("@")
        parts[0] = parts[0].replace(".","")
        #print(parts)
        for x in range(len(parts[0])):
            if parts[0][x] == "+":
                parts[0] = parts[0][0:x]
                break
                
        #print(parts[0])       
        self.ans.add(parts[0]+","+parts[1])
        #print(parts)
        
