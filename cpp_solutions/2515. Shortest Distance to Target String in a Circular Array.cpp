class Solution {
public:
    void print_vec(vector<string> t) {
        for(auto it : t) {
            cout << it << " ";
        }
    }
    int closetTarget(vector<string>& words, string target, int startIndex) {
        vector<string> temp;
        int n = words.size();
        for(auto it : words){
            temp.emplace_back(it);
        }
        for(auto it : words){
            temp.emplace_back(it);
        }
        for(auto it : words){
            temp.emplace_back(it);
        }
        
        int start = n + startIndex;
        // move left and right to check
        int ans = 100000;
        for(int i = start; i < temp.size(); ++i) {
            if (temp[i] == target){
                ans = min(ans, i - start);
            }
        }

        for(int i = start; i >= 0; --i) {
            if (temp[i] == target){
                ans = min(ans, start - i);
            }
        }

        if(ans!=100000){
            return ans;
        } else {
            return -1;
        }
    }
};
