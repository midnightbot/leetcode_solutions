class Solution {
public:
    int divisorSubstrings(int num, int k) {
        int count = 0;
        
        
        auto revs = std::to_string(num);
        for(int x=0;x<revs.size()-k+1;x++){
            ///cout << revs.substr(x,x+k)<<"\n";
            auto temp = revs.substr(x,k);
            int comp = stoi(temp);
            //cout << comp << '\n' << x << "--" << x+k << '\n';
            if (comp!=0 && num%comp==0){
                count++;
            } 
        }
        
        return count;
        
    }
};
