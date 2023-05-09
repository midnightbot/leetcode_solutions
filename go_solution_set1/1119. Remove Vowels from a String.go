func removeVowels(s string) string {
    ans := ""
    for _, x:= range s{
        if x!='a' && x!='e' && x!='o' && x!='i' && x!='u'{
            ans+= string(x)
        }
    }
    return ans
}
