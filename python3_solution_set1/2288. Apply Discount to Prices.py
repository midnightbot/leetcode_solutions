class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        
        temp = sentence.split(" ")
        
        for indx,wrds in enumerate(temp):
            if wrds[0]!='$' or not wrds[1:].isnumeric():
                continue
                
            else:
                tempo = int(wrds[1:])
                tempo = (100-discount)/100 * tempo
                
                tempo = "{:.2f}".format(tempo)
                temp[indx] = "$" + str(tempo)
                
        return " ".join(temp)
        
