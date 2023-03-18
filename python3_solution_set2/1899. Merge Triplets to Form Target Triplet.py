class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        comp = []

        for x,y,z in triplets:
            if x<=target[0] and y<=target[1] and z<=target[2]:
                comp.append([x,y,z])


        a = -1
        b = -1
        c = -1

        for x,y,z in comp:
            a = max(a,x)
            b = max(b,y)
            c = max(c,z)

        return [a,b,c] == target
