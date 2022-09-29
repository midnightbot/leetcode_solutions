class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        #### Minute Details############
        ## max operation = len(nums) -1 -> just leaving a single number in array
        ## min operation = 0 -> already palindrome
        ##############################
        
        ## idea -> try to balance sum from both sides
        ## once sum is balanced repeat the above procedure on the left array
        ## kind of **two pointer approach**
        
        ## Space Complexity : O(1)
        ## Time Complexity : O(n)
        
        n = len(nums)
        
        i = 0
        j = n - 1
        op = 0
        while i < j:
            sum1 = nums[i]
            sum2 = nums[j]
            #print(i,j, "--")
            og_i = i
            og_j = j
            this_count = 0
            while sum1!=sum2: ## trying to make sum equal from both sides
                this_count+=1
                #print(sum1,sum2)
                if i < j:  ## if some elements to be considered are left in array
                    if sum2 > sum1:  ## if right_sum > left_sum add items in left sum
                        i+=1
                        sum1+=nums[i]

                    elif sum1 > sum2:  ## if left_sum > right_sum add items in right_sum
                        j-=1
                        sum2+=nums[j]
                else: ## left array from og_i .. og_j is to be made a single number
                    ## hence number of operations required would be og_j - og_i
                    ## example [....,1,2,3,4,......]
                    sum1 = sum2
                    i = j
                    this_count = og_j - og_i
            #print(this_count)
            op+=this_count
            i+=1
            j-=1
        return op
