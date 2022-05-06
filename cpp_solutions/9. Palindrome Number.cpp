class Solution {
public:
    bool isPalindrome(int x) {
        auto s = std::to_string(x);
        auto revs = std::to_string(x);
        
        reverse(revs.begin(), revs.end());
        //cout << s;
        for (int x=0 ; x< s.length();x++){
            if(s[x]!=revs[x]){
                return false;
            }
        }
        return true;
    }
};
