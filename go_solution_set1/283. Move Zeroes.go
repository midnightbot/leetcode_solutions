func moveZeroes(nums []int)  {
    ans := []int{}
    cnt := 0
    for _, val := range nums{
        if val == 0{
            cnt+=1
        } else{
            ans = append(ans, val)
        }
    }

    for i:=0; i<cnt;i++{
        ans = append(ans,0)
    }

    for i:=0; i<len(nums);i++{
        nums[i] = ans[i]
    }
    
}
