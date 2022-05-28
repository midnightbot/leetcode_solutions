class Solution {
public:
    bool digitCount(string num) {
        
        vector<int> counter(10,0);
        
        for (char ch:num){
            int temp = ch -'0';
            //cout << temp;
            counter[temp]+=1;
        }
        
        for (int x=0;x<num.length();x++){
            if (num.at(x) - '0'!=counter[x]){
                return false;
            }
        }
        return true;
        
    }
};
