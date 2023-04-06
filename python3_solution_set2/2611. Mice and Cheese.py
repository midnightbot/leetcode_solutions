class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        ## mice1 k cheese
        ## mice2 n-k cheese

        ## mice1 will eat the cheese where reward1 - reward2 is greatest
        ## simple sorting
        temp = []

        for x,y in zip(reward1, reward2):
            temp.append([x-y,x,y])

        temp = sorted(temp, key = lambda x:-x[0])
        mice1 = sum([x[1] for x in temp[:k]])
        mice2 = sum([x[2] for x in temp[k:]])
        return mice1 + mice2
