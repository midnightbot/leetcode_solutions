class Solution:
    def distinctNames(self, ideas: List[str]) -> int:

        hasher = {chr(97+x):set() for x in range(26)}
        ans = 0
        for x in ideas:
            hasher[x[0]].add(x[1:])
        #print(hasher)

        for key1 in hasher:
            list1 = hasher[key1]
            for key2 in hasher:
                list2 = hasher[key2]
                if key1 > key2:
                    overlap = len(list1 & list2)
                    ans+=(len(list1) - overlap) * (len(list2) - overlap)
        return ans*2
