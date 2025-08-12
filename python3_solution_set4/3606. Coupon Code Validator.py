class Solution:
    def check_valid_code(self, s):
        if s == "":
            return False
        for x in s:
            if x not in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_':
                return False
        return True

    def check_valid_business(self, s):
        if s not in ['electronics', 'grocery', 'pharmacy', 'restaurant']:
            return False
        return True
    

    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:

        # return [code[i] if (self.check_valid_code(code[i]) and self.check_valid_business(businessLine[i] and isActive[i])) else 0 for i in range(len(code))]
        ans = {}
        for x in range(len(code)):
            if self.check_valid_code(code[x]) and self.check_valid_business(businessLine[x]) and isActive[x]:
                if businessLine[x] not in ans:
                    ans[businessLine[x]] = []
                ans[businessLine[x]].append(code[x])
        for x in ans:
            ans[x] = sorted(ans[x])
        # print(ans)
        return ans.get("electronics", []) + ans.get("grocery", []) + ans.get("pharmacy", []) + ans.get("restaurant", [])
