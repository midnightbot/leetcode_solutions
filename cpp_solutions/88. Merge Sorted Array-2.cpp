class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        vector<int> temp(m,-1);
        
        for(int x=0;x<m;x++){
            temp[x] = nums1[x];
        }
        int i = 0;
        int j = 0;
        int c = 0;
        while (i < m && j < n){
            
            if (temp[i] < nums2[j]){
                nums1[c] = temp[i];
                i+=1;
            }
            else{
                nums1[c] = nums2[j];
                j+=1;
            }
            c+=1;
        }
        //cout << i << j;
        if (i < m){
            for(int k = i ; k < m ; k++){
                nums1[c] = temp[k];
                
                c+=1;
            }
            
        }
        
        if(j < n){
            for(int k = j ; k < n ; k++){
                nums1[c] = nums2[k];
                
                c+=1;
            }
        }
        
        
    }
};
