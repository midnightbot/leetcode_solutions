#include <iostream>
#include <algorithm>
using std::cout;
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string ans;
        int i = 0;
        int sizes = 200;
        for(int x= 0; x< strs.size();x++){
            if (strs[x].length() < sizes){
                sizes = strs[x].length();
            }
            //cout << strs[x].length();
        }
        
        for(int x = 0; x< sizes; x++){
            char compare = strs[0].at(x);
            bool prob = false;
            //cout << compare;
            for(i=0;i<strs.size();i++){
                if (strs[i].at(x)!=compare){
                    prob = true;
                    break;
                }
                
            }
            
            if(prob == true){
                return ans;
            }
            else{
                ans+=compare;
            }
        }
        return ans;
    }
};
