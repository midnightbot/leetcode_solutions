func isAnagram(s string, t string) bool {
    temp1 := []int{}
    temp2 := []int{}
    for x:=0; x<26; x++{
        temp1 = append(temp1,0)
        temp2 = append(temp2,0)
    }
    for _,x := range s{
        temp1[int(x) - int('a')]+=1
    }
    for _,x := range t{
        temp2[int(x) - int('a')]+=1
    }

    for x:=0; x<26; x++{
        if temp1[x]!=temp2[x]{
            return false
        }
    }
    return true
}
