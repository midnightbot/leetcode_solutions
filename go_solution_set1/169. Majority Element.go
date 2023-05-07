import (
    "math"
)
func majorityElement(nums []int) int {
    counter := make(map[int]int)

    for _, val := range nums{
        _,present := counter[val]
        if present{
            counter[val]+=1
        } else {
            counter[val] = 1
        }
    }

    tmp := int(math.Floor(float64(len(nums))/2))
    
    for key, val := range counter{
        if val > tmp {
            return key
        }
    }

    return 0
}
