class Solution {
public:
    string removeStars(string s) {
        stack<char> stacks;
        for(char it : s) {
            if (string(1,it) != "*" ) {
                stacks.push(it);
            } else {
                while(string(1,stacks.top()) =="*") {
                    stacks.pop();
                }
                stacks.pop();
            }
        }
        
        string ans = "";
        while (!stacks.empty()) {
            ans+=stacks.top();
            stacks.pop();
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};
