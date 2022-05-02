class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        
        vector<int> even(5000,-1);
        vector<int> odd(5000,-1);
        
        int i = 0;
        int j = 0;
        
        for (int a:nums){
            if (a%2==0){
                even[i] = a;
                i+=1;
            }
            else{
                odd[j] = a;
                j+=1;
            }
        }
        
        int n = nums.size();
        vector<int> ans(n,0);
        
        int c =0;
        i = 0;
        while (i < even.size() and even[i]!=-1){
            ans[c] = even[i];
            c+=1;
            i+=1;
            
        }
        i = 0;
        while (i < odd.size() and odd[i]!=-1){
            ans[c] = odd[i];
            c+=1;
            i+=1;
            
        }
        
        return ans;
        
    }
};
