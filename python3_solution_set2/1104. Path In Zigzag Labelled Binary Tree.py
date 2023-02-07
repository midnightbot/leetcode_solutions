class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        def find_level(num):
            for x in range(0,100):
                if 2**x > num:
                    return x-1
                elif 2**x == num:
                    return x
            
        def find_parent(num, level):
            
            #space = math.ceil(space/2)

            if level%2==0:
                space = num - 2**level + 1
                #print(space)
                #space = num - (2**level)
                space = math.ceil(space/2)
                
                #print(space, "here")
                return 2**(level) - space
            else:
                ## new defn of space
                space = 2**level - ((num - 2**level)//2)*2 - (num - 2**level)%2
                space = math.ceil(space/2)
                #print(space)
                return 2**(level-1) + space - 1

        #label = 2
        level = find_level(label)
        #print(level, "level")
        #print(find_parent(label, level), "on")
        ans = [label]
        while level>=1:
            label = find_parent(label,level)
            level-=1
            #print(new_num,level)
            ans.append(label)
        #ans.append(1)
        return ans[::-1]
