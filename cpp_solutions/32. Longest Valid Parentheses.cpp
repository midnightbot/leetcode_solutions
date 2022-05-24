class Solution {
public:
    int longestValidParentheses(string s) {
        
        stack<int> stack;
        int ans = 0;
        stack.push(-1);
        for(int x=0;x<s.length();x++){
            if (s.at(x) == '('){
                stack.push(x);
            }
            else{
                stack.pop();
                if (stack.size()!=0){
                    ans = max(ans, x - stack.top());
                }
                else{
                    stack.push(x);
                }
            
            }
        }
        return ans;
        
    }
};
