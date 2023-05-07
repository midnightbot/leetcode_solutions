func twoSum(nums []int, target int) []int {
    m := make(map[int]int)

    for i:=0 ; i < len(nums); i++ {
        val, present := m[target - nums[i]]
        if present {
            return []int{i, val}
        } else {
            m[nums[i]] = i
        }
    }  

    return []int{}
}
