class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        int carry = 1;
        
        for(int x = digits.size()-1;x>=0;x--){
            
            if (carry == 1){
                if(digits[x]+1!=10){
                    ++digits[x];
                    carry = 0;
                }
                else{
                    digits[x] = 0;
                    carry = 1;
                }
            }
            else{
                break;
            }
        }
        if (carry==1){
            digits.insert(digits.begin(),1);
        }
        return digits;
    }
};
