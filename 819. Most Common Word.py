##ss
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        dicts = {}
        banned.append(" ")
        banned.append("")
        paragraph = paragraph.lower()
        paragraph = paragraph.replace("!"," ")
        paragraph = paragraph.replace("?"," ")
        paragraph = paragraph.replace("'"," ")
        paragraph = paragraph.replace(","," ")
        paragraph = paragraph.replace(";"," ")
        paragraph = paragraph.replace("."," ")
       
        paragraphs = paragraph.split(" ")
        
        for x in range(len(paragraphs)):
            if paragraphs[x] in dicts.keys():
                dicts[paragraphs[x]]+=1
                
            else:
                dicts[paragraphs[x]] = 1
                
        ans = []
        for x in dicts.keys():
            ans.append([dicts[x],x])
            
        ans = sorted(ans,reverse = True, key = lambda x:x[0])
        
        for x in range(len(ans)):
            if ans[x][1] not in banned:
                return ans[x][1]
        
        
