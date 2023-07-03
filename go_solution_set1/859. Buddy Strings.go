func find_map(s string) map[string]int{
    f := make(map[string]int)
    for x:=0;x<len(s);x++{
        _,ok := f[string(s[x])]
        if ok{
            f[string(s[x])]+=1
        } else {
            f[string(s[x])] = 1
        }
    }
    return f
}
func buddyStrings(s string, goal string) bool {
    
    cnt := 0
    smap :=find_map(s)
    goalmap := find_map(goal)
    for x:=0; x<len(s);x++{
        if s[x]!=goal[x]{
            cnt++
        }
    }
    if !reflect.DeepEqual(smap,goalmap){
        return false
    }
    if cnt == 2{
        return true
    }
    if cnt == 0{
         for _,val := range smap{
             if val>=2{
                 return true
             }
         }
    }
    
    
    return false
}
