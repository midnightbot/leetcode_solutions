class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        
        int count = 0;
        
        for(int x=left; x<=right;x++){
            if (isittrue(x)){
                count+=1;
            }
        }
        
        return count;
        
    }
    bool isittrue(int n){
        string temp = std::bitset<20>(n).to_string();
        int c  = 0;
        for(char ch: temp){
            if (ch == '1'){
                c+=1;
            }
        }
        //return std::bitset<8>(n).to_string();
        if (c==2 || c==3 || c==5 || c==7 || c==11 || c==13 || c==17 || c==19){
            return true;
        }
        return false;
    }
};
