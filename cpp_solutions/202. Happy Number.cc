class Solution {
public:
    
    int new_num(int n) {
        string num = to_string(n);
        int ans = 0;
        for(auto it : num) {
            int k = stoi(string(1, it));
            ans+= k * k;
        }
        return ans;
    }
    bool isHappy(int n) {
        
        int its = 0;
        while (its < 30 && n!=1) {
            int k = new_num(n);
            n = k;
            ++its;
        }
        if (n == 1) {return true;}
        return false;
    }
};
