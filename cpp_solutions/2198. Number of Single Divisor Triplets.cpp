class Solution {
public:
    long long singleDivisorTriplet(vector<int>& nums) {
        unordered_map<int,long long int> freqs;
        long long ans = 0;
        for(int c: nums){
            if (freqs.find(c)!=freqs.end()){
                freqs[c]+=1;
            }
            else{
                freqs.insert({c,1});
            }
        }
        
        for(int x=1; x<=100;x++){
            for(int y=x;y<=100;y++){
                for (int z=y; z<=100;z++){
                    if ((freqs.find(x)!=freqs.end()) && (freqs.find(y)!=freqs.end()) && (freqs.find(z)!=freqs.end()) && valid(x,y,z)){
                        if (x==y){
                            ans+= freqs[x] * (freqs[x]-1)/2 * freqs[z];
                        }
                        else if(y==z){
                            ans+= freqs[x] * freqs[y] * (freqs[y]-1)/2;
                        }
                        else{
                            ans+= freqs[x] * freqs[y] * freqs[z];
                        }
                    }
                }
            }
        }
        
        return ans * 6;
        
    }
    bool valid(int i, int j , int k){
        int sums = i + j + k;
        
        if (sums%i==0){
            return sums%j!=0 && sums%k!=0;
        }
        else if(sums%j==0){
            return sums%k!=0;
        }
        else{
            return sums%k == 0;
        }
    }
};
