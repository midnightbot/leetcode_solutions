##ss
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ""
        

        def make(num,ans):
            #print(num,"anish",ans)
            if num == 1:
                ans+="1"
                return "1"
            elif num!=0:
                ans+=make(num-1,ans)
                #print("isnide",ans,num)
                return convert(ans)
            
            elif num == 0:
                return ans
        
        
        
        def convert(ans):
            final_ans = ""
            c = 1
            if len(ans) == 1:
                return ans[0]+ans[0]
            
            for x in range(1,len(ans)):
                if ans[x] == ans[x-1]:
                    c+=1
                    
                else:
                    final_ans+=str(c)
                    final_ans+=ans[x-1]
                    c = 1
            final_ans+=str(c)
            final_ans+=ans[-1]
            #print(ans,final_ans,"converting")
            return final_ans
        
        return ((make(n,ans)))
