class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        sum1 = []
        sum2 = []
        sum3 = []
        for x in range(len(firstWord)):
            sum1.append(ord(firstWord[x]) - 97)
          
        for y in range(len(secondWord)):
            sum2.append(ord(secondWord[y]) - 97)
            
        for z in range(len(targetWord)):
            sum3.append(ord(targetWord[z]) - 97)
        
        strings = [str(integer) for integer in sum1]
        a_string = "".join(strings)
        an_integer = int(a_string)
        
        strings1 = [str(integer) for integer in sum2]
        a1_string = "".join(strings1)
        an1_integer = int(a1_string)
        
        strings2 = [str(integer) for integer in sum3]
        a2_string = "".join(strings2)
        an2_integer = int(a2_string)
        
        if an_integer+an1_integer == an2_integer:
            return True
        else:
            return False
            
        
