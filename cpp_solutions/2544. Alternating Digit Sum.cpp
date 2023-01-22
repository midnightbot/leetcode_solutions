class Solution {
public:
    int alternateDigitSum(int n) {
        string s = to_string(n);
        int ans = 0;
        for(int x=0; x<s.size();++x){
            if (x%2==0){
                ans+=int(s.at(x))-int('0');
            } else{
                ans-=int(s.at(x)-int('0'));
            }
        }
        return ans;
    }
};
