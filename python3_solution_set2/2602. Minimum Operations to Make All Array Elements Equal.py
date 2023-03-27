class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        
        ## all numbers that are lesser than q are to be increased
        ## all number that are greater than q are to be decreased
        ## sort nums and find the number of elements smaller than query and number of elements larger than query
        ## to increase say [1,2,3] to 4
        ## 4*(number_of_elements) - sum(arr)  = 12 - 6 = 6 operations
        ## similarly for greater elements
        ## O(nlogn)
        nums.sort()

        ans = []
        temp = list(accumulate(nums))
        n = len(nums)
        for q in queries:
            indx = bisect.bisect_right(nums, q)
            if indx > 0:
                sum1 = temp[indx-1]
            else:
                sum1 = 0
            sum2 = temp[-1] - sum1
            c = (q*indx - sum1) + (sum2 - q*(n-indx))
            

            ans.append(c)

        return ans
