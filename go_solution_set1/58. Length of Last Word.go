import "fmt"
func lengthOfLastWord(s string) int {
    temp := strings.Split(s, " ")
    ans := 0

    for _, x := range temp{
        if x!=""{
            ans = len(x)
        }
    }

    return ans
}
