##ss
class Solution:
    def arrangeWords(self, text: str) -> str:
        
        text = text.lower()
        texts = text.split(" ")
        texts = sorted(texts, key = lambda x:(len(x)))
        print(texts)
        
        ans = " ".join(texts)
        print(ans)
        ret_ans = chr(ord(ans[0])-32) + ans[1:]
        
        return ret_ans
