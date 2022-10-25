class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        
        
        numseven = sorted([x for x in nums if x%2==0])
        numsodd = sorted([x for x in nums if x%2!=0])
        
        targeteven = sorted([x for x in target if x%2==0])
        targetodd = sorted([x for x in target if x%2!=0])
        
        
        sum1 = sum([abs(numseven[x]-targeteven[x]) for x in range(len(numseven))])
        sum2 = sum([abs(numsodd[x]-targetodd[x]) for x in range(len(numsodd))])
        
        return (sum1 + sum2)//4
        
