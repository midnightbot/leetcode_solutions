class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        list1=[]
        list1[:0]=keyboard
        
        list2 = []
        list2[:0] = word
        ans = 0
        counter = 0
        for x in range(len(list2)):
            for y in range(len(list1)):
                if(list1[y]==list2[x]):
                    #print("x:", int(x))
                    ans+= (abs(counter - y))
                    #print(ans)
                    counter = y
                    
        return ans
