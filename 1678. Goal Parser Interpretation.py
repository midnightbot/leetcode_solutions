class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        print(command[0])
        
        for x in range(len(command)):
            if command[x]=="G":
                ans+="G"
                
            elif command[x]=="(" and command[x+1]==")":
                ans+="o"
               
                x=x+1
            elif command[x]=="(" and command[x+1]=="a":
                ans+="al"
                
                x=x+3
        return str(ans)
        
