//ss
class Solution {
public:
    string largestGoodInteger(string num) {
        int size = num.length();
        int ans = -1;
        
        for(int x =0; x<size-3+1;x++){
            if (num.at(x) == num.at(x+1) && num.at(x+1) == num.at(x+2)){
                //cout << stoi(num.substr(x,3)) << "\n";
                ans = max(ans, stoi(num.substr(x,3)));
                //return num.substr(x,x+2);
            }
        }
        
        if (ans == -1){return "";}
        else if(ans == 0) {return "000";}
        else {return to_string(ans);}
        
    }
};
