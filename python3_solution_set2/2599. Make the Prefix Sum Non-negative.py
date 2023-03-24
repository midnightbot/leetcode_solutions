class Solution:
    def makePrefSumNonNegative(self, nums: List[int]) -> int:
        ## use a queue
        ## add to queue if there is no negative
        ## once we find prefix sum is negative, put this number to last and add the number which will keep the prefix sum positive
        ## [6,-6,-3,3,1,5,-4,-3,-2,-3,4,-1,4,4,-2,6,0]
        ## this example moving -6 is required


        operations = 0
        pre_sum = 0
        negative = []
        for x in nums:
            pre_sum+=x
            heapq.heappush(negative, x)
            if pre_sum < 0: ## if the pre_sum becomes negative remove the largest seen negative number till now and put it at the end
                operations+=1
                top = heapq.heappop(negative)
                pre_sum-=top
                nums.append(top)
            
        return operations
