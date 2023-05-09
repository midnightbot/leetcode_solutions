func getConcatenation(nums []int) []int {
    ans := []int{}
    for x:=0; x<len(nums);x++{
        ans = append(ans,0)
        ans = append(ans, 0)
    }
    n := len(nums)
    for x:=0; x<len(nums);x++{
        ans[x] = nums[x]
        ans[x+n] = nums[x]
    }


    return ans
}
