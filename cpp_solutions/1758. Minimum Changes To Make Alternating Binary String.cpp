class Solution {
public:
    int minOperations(string s) {
        
        int n = s.length();
        
        string str1 = "0";
        string str2 = "1";
        
        for(int x=0;x<n-1;x++){
            if (str1.back() == '0'){
                str1+='1';
            }
            else{
                str1+='0';
            }
        }
        
        for(int x=0;x<n-1;x++){
            if (str2.back() == '0'){
                str2+='1';
            }
            else{
                str2+='0';
            }
        }
        
        return std::min(diffs(s,str1),diffs(s,str2));
        
        
    }
    
    int diffs(string s1, string s2){
        
        int ans = 0;
        
        for (int x=0;x<s1.length();x++){
            if(s1.at(x)!=s2.at(x)){
                ans+=1;
            }
        }
        return ans;
    }
};
