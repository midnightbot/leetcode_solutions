class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        sentence = sentence.split(" ")
        for x in range(1,len(sentence)):
            if sentence[x][0] != sentence[x-1][-1]:
                #print(sentence[x][0], sentence[x-1])
                return False

        return sentence[-1][-1] == sentence[0][0]
